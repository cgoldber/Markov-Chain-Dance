# Title : Markov Chain Dancer

# Description
The Markov Chain Dancer generates dance choreography based on probabilities and then displays the sequential moves in the dance. There are 13 possible dance moves included in this implementation. 

The starting move is selected based on a prior probability distribution that indicates how likely it is for each move to be the starting move in a dance. The Markov Chain Dancer selects the next dance move by considering the probabilities of the next possible dance move given the current dance move. This process continues until the dance consists of a set number of moves (chosen by user).

After the dance is created using Markov reasoning, various video clips of each move are concatenated together sequentially to display the progression of the dance.

I would like to extend my sincerest gratitude to esteemed dance major at Bowdoin College, Dylan Richmond, for his invaluable participation in my project. I consulted Mr. Richmond for his expertise in the field of dance. For one thing, he provided me the names of 13 dance moves that he enjoys incorporating into his choreography. Mr. Richmond also used his experience choregraphing dances to generate the prior and transition probabilities. Finally, Mr. Richmond demonstrated each dance move for the individual video clips that make up the final sequence. Thanks Dylan!

# Running the Code
Installations -
Python Packages: numpy, pandas, openpyxl, moviepy
Other Packages: ffmpeg (https://ffmpeg.org/), imagemagick (https://imagemagick.org/index.php)

Where to Run - 
Run the MarkovDance.py program. Be sure that the Examples and Assests folders, as well as the Probability Table excel sheet are in the same path as the python program.

User Input - 
The user will be prompted to input how many dance moves they would like to incorporate into the dance. They will continue to be prompted until they put one of the following values: 5, 10, or 15.


# Project Development Reflection
Q1. Describe how the system is personally meaningful to you.
As a student at Bowdoin College, I am constantly awed and inspired by the creative people around me. 

Q2. Explain how working on it genuinely challenged you as a computer scientist.How did you push yourself outside of your comfort zone? Why was this an important challenge for you?

Q3. What are the next steps for you going forward?

Q4. Is your system creative?
