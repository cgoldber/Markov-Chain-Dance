import cv2
import numpy as np
import glob

IMG_LEN = 2
NUM_MOVES = 10
STARTING_MOVE = "B"

class MarkovDancer:
    def __init__(self, transition_matrix):
        """Simulates a dancer that relies on a simple Markov chain to choose next dance move.
           Args:
                transition_matrix (dict): transition probabilities
        """
        self.transition_matrix = transition_matrix
        self.moves = list(transition_matrix.keys())

    def get_next_move(self, current_move):
        """Decides which move to choose next based on the current move.
           Args:
               current_move (str): the current dance move being displayed.
        """
        return np.random.choice(
            self.moves,
            p=[self.transition_matrix[current_move][next_move] \
            for next_move in self.moves]
        )

    def compose_dance(self, current_move="A", num_moves=5):
        """Generates a sequence of notes.
           Args:
                current_move (str): the dance move that is currently being displayed.

                song_length (int): how many dance moves we should generate for the dance.
        """
        dance = [current_move]
        while len(dance) < num_moves:
            next_move = self.get_next_move(current_move)
            dance.append(next_move)
            current_move = next_move

        return dance

    def get_move_images(self, dance, max_width, max_height):
        img_array = []
        path = 'dancePics/dance'
        for move in dance:
            img = cv2.imread(path + move + ".jpg") #prob gonna only wanna get each image once

            # Calculate the padding needed to reach the maximum dimensions
            top_pad = (max_height - img.shape[0]) // 2
            bottom_pad = max_height - img.shape[0] - top_pad
            left_pad = (max_width - img.shape[1]) // 2
            right_pad = max_width - img.shape[1] - left_pad

            padded_img = cv2.copyMakeBorder(img, top_pad, bottom_pad, left_pad, right_pad, cv2.BORDER_CONSTANT, value=(255, 255, 255))
            img_array.append(padded_img)
        return img_array

    def write_dance_video_file(self, dance):
        """Write out a collection of dance move images (i.e, a dance!) to a file.
           Args:
               dance (list): moves in the dance
        """
        # get maximum dimensions
        max_width = 0
        max_height = 0
        for filename in glob.glob('dancePics/*.jpg'):
            img = cv2.imread(filename)
            height, width, layers = img.shape
            if width > max_width:
                max_width = width
            if height > max_height:
                max_height = height

        img_array = self.get_move_images(dance, max_width, max_height)
        
        out = cv2.VideoWriter('vids/markovDancer.avi',cv2.VideoWriter_fourcc(*'XVID'), IMG_LEN, (max_width, max_height))
        
        for img in img_array:
            out.write(img)
        out.release()


def main():
    dance_maker = MarkovDancer({
        "A": {"A": 0.3, "B": 0.4, "C": 0.3},
        "B": {"A": 0.7, "B": 0.2, "C": 0.1},
        "C": {"A": 0.1, "B": 0.7, "C": 0.2}
    })
    new_dance = dance_maker.compose_dance(current_move=STARTING_MOVE, num_moves=NUM_MOVES)


    print("Here's my latest dance:", new_dance)
    print("Writing dance to file...")
    dance_maker.write_dance_video_file(new_dance)
    print("Process completed!")


if __name__ == "__main__":
    main()
