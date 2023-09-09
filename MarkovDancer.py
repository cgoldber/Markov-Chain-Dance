import cv2
import numpy as np
import glob
from moviepy.editor import VideoFileClip, clips_array
import pandas as pd
import datetime
import os


NUM_MOVES = 20

class RetrieveProbabilities:
    def __init__(self):
        print("Retrieving Transition and Prior Probabilities")
    
    def retrieve_trans_mat(self):
        """Reads excel sheet that records the probability that each dance move will come next preconditioned on the current dance move.
        """
        return pd.read_excel("CC Dance.xlsx", sheet_name = "Normalized Matrix", index_col=0, header=0)
        
    def retrieve_priors(self):
        """Reads excel sheet that records the probability that each dance move will come first in the sequence.
        """
        return pd.read_excel("CC Dance.xlsx", sheet_name = "Normalized Prior", index_col=0, header=0)


class MarkovDancer:
    def __init__(self, transition_matrix, priors):
        """Simulates a dancer that relies on a simple Markov chain to choose next dance move.
        Args:
               transition matrix (dict): the probabilities of transitioning from each move to every other move
        """
        self.transition_matrix = transition_matrix
        self.priors = priors
        self.moves = list(transition_matrix.columns)
    
    def get_first_move(self):
        """Decides first move of sequence based on priors.
        """
        return np.random.choice(
            self.moves,
            p=[self.priors.loc[move]["Probability"] for move in self.moves]
        )

    def get_next_move(self, current_move):
        """Decides which move to choose next based on the current move.
           Args:
               current_move (str): the current dance move being displayed.
        """
        return np.random.choice(
            self.moves,
            p=[self.transition_matrix.loc[current_move][next_move] \
            for next_move in self.moves]
        )

    def compose_dance(self, num_moves=5):
        """Generates a sequence of notes.
           Args:
                current_move (str): the dance move that is currently being displayed.

                song_length (int): how many dance moves we should generate for the dance.
        """
        current_move = self.get_first_move()
        dance = [current_move]
        while len(dance) < num_moves:
            next_move = self.get_next_move(current_move)
            dance.append(next_move)
            current_move = next_move

        return dance

    def write_dance_video_file(self, dance):
        """Write out a collection of dance move images (i.e, a dance!) to a file.
           Args:
               dance (list): moves in the dance
        """
        video_clips = [VideoFileClip('Move Videos/' + move + ".mov") for move in dance]
        final_clip = clips_array([[clip] for clip in video_clips])
        final_clip = final_clip.resize(newsize=(1920, 1080))
        final_clip.write_videofile("Final Vids/" + str(datetime.datetime.now()) + ".mp4", codec="libx264", fps=24)
        

def main():
    #os.environ["IMAGEIO_FFMPEG_EXE"] = "FFMPEG Download/ffmpeg-6.0"
    prob_retriever = RetrieveProbabilities()
    transition_matrix = prob_retriever.retrieve_trans_mat()
    priors = prob_retriever.retrieve_priors()

    dance_maker = MarkovDancer(transition_matrix, priors)
    new_dance = dance_maker.compose_dance(num_moves=NUM_MOVES)

    print("Here's my latest dance:", new_dance)
    print("Writing dance to file...")
    dance_maker.write_dance_video_file(new_dance)
    print("Process completed!")


if __name__ == "__main__":
    main()
