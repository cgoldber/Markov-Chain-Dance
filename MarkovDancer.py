import numpy as np
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips, clips_array
import pandas as pd
import datetime


class Communicator:
    def __init__(self):
        print("Hello, welcome to my Markov Dancer")
    
    def get_num_moves(self):
        """Asks user to choose how many moves shall be included in the dance (5, 10 or 15).
        """
        num_moves = input("Would you like to incorporate 5, 10, or 15 dance moves into the choreography? ")
        while num_moves != "5" and num_moves != "10" and num_moves != "15":
            num_moves = input("Try again, this Markov Dancer only accepts 5, 10, or 15 moves: ")
        return int(num_moves)


class RetrieveProbabilities:
    def __init__(self):
        print("Retrieving Transition and Prior Probabilities")
    
    def retrieve_trans_mat(self):
        """Reads excel sheet that records the probability that each dance move will come next preconditioned on the current dance move.
        """
        return pd.read_excel("Probability Table.xlsx", sheet_name = "Normalized Matrix", index_col=0, header=0)
        
    def retrieve_priors(self):
        """Reads excel sheet that records the probability that each dance move will come first in the sequence.
        """
        return pd.read_excel("Probability Table.xlsx", sheet_name = "Normalized Prior", index_col=0, header=0)


class MarkovDancer:
    def __init__(self, transition_matrix, priors):
        """Simulates a dancer that relies on a simple Markov chain to choose next dance move.
        Args:
               transition matrix (dict): the probabilities of transitioning from each move to every other move
               priors (dict): the probabilities of starting with each move
        """
        self.transition_matrix = transition_matrix
        self.priors = priors
        self.moves = list(transition_matrix.columns)
    
    def get_first_move(self):
        """Decides first move of sequence based on prior probabilities.
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

    def compose_dance(self, num_moves):
        """Generates a sequence of notes based on transition probabilities.
           Args:
                num_moves (int): how many dance moves are included in the dance.
        """
        current_move = self.get_first_move()
        dance = [current_move]
        while len(dance) < num_moves:
            next_move = self.get_next_move(current_move)
            dance.append(next_move)
            current_move = next_move

        return dance
    

class VideoGenerator():
    def __init__(self, dance):
        print("Generating video representation of dance...")
        self.dance = dance

    def loop_vid(self, clip, start_time, total_duration):
        """Concatenate videos of the same dance move so that it loops until the video ends.
           Args:
               clip (VideoFileClip): video clip to be looped
               start_time (float): time that the current looped video should start displaying
               total_duration (float): total time of all the chosen dance moves
        """
        num_loops = int(total_duration // clip.duration) + 1
        loop_clip = concatenate_videoclips([clip] * num_loops)
        loop_clip = loop_clip.set_start(start_time)
        return loop_clip
    
    def annotate(self, move, clip, start_time):
        """Adds caption describing dance move to each clip.
           Args:
               move (string): current dance move
               clip (VideoFileClip): video clip to be captioned
        """
        cap = TextClip(move, fontsize=70, color='white')
        cap = cap.set_position(("center", 850))
        cap = cap.set_duration(clip.duration).set_start(start_time)
        return CompositeVideoClip([clip, cap])
    
    def edit_clips(self, clips, total_duration):
        """Processes each clip to make them visually appealing.
           Args:
               dance (list): current dance move
               clips (list): video clip to be captioned
               total_duration (float): sum of individual video clip durations
        """
        start_time = 0
        edited_clips = []
        for move, clip in zip(self.dance, clips):
            clip = clip.set_audio(None).resize(newsize=(650, 960)) #adjust clip size and volume
            #loop clip so that once played, it continues until video terminates
            loop_clip = self.loop_vid(clip, start_time, total_duration)
            captioned_clip = self.annotate(move, loop_clip, start_time) #caption clip

            edited_clips.append(captioned_clip)
            start_time += clip.duration 
        return edited_clips
    
    def align_array(self, clips):
        """Aligns clip array so that there are 5 video clips per row.
           Args:
               clips (list): video clips in dance
        """
        clip_array = []
        for i in range(0, len(clips), 5):
            row = clips[i:i+5]
            clip_array.append(row)
        return clips_array(clip_array, bg_color=(0, 0, 0))
        
    def write_dance_video_file(self):
        """Write out a collection of dance move clips to a file.
           Args:
               dance (list): moves in the dance
        """
        raw_vids = [VideoFileClip('Assets/' + move + ".mov") for move in self.dance]
        total_duration = sum(clip.duration for clip in raw_vids)

        #put clips into the right format
        edited_clips = self.edit_clips(raw_vids, total_duration)
        clip_arry = self.align_array(edited_clips)
        clip_arry = clip_arry.set_end(total_duration) #cut off once final move finishes
        #write to file
        clip_arry.write_videofile("Examples/" + str(datetime.datetime.now()) + ".mp4", fps=24)
  

def main():
    myCommunicator = Communicator()
    num_moves = myCommunicator.get_num_moves()

    prob_retriever = RetrieveProbabilities()
    transition_matrix = prob_retriever.retrieve_trans_mat()
    priors = prob_retriever.retrieve_priors()

    dance_maker = MarkovDancer(transition_matrix, priors)
    new_dance = dance_maker.compose_dance(num_moves)
    print("Here's my latest dance:", new_dance)

    video_generator = VideoGenerator(new_dance)
    video_generator.write_dance_video_file()

    print("Process completed!")


if __name__ == "__main__":
    main()
