# Markov Chain Dancer

## Description
The Markov Chain Dancer generates dance choreography based on probabilities and then displays the sequential moves in the dance. There are 13 possible dance moves included in this implementation. 

The starting move is selected based on a prior probability distribution that indicates how likely it is for each move to be the starting move in a dance. The Markov Chain Dancer selects the next dance move by considering the probabilities of the next possible dance move given the current dance move. This process continues until the dance consists of a set number of moves (chosen by user).

After the dance is created using Markov reasoning, various video clips of each move are concatenated together sequentially to display the progression of the dance.

I would like to extend my sincerest gratitude to esteemed dance major at Bowdoin College, Dylan Richmond, for his invaluable participation in my project. I consulted Mr. Richmond for his expertise in the field of dance. For one thing, he provided me the names of 13 dance moves that he enjoys incorporating into his choreography. Mr. Richmond also used his experience choregraphing dances to generate the prior and transition probabilities. Finally, Mr. Richmond demonstrated each dance move for the individual video clips that make up the final sequence. Thanks Dylan!

## Running the Code
### Installations
Python Packages: numpy, pandas, openpyxl, moviepy

Other Packages: ffmpeg (https://ffmpeg.org/), imagemagick (https://imagemagick.org/index.php)

### Where to Run

Run the MarkovDance.py program. Be sure that the Examples and Assests folders, as well as the Probability Table excel sheet are in the same path as the python program.

### User Input

The user will be prompted to input how many dance moves they would like to incorporate into the dance. They will continue to be prompted until they put one of the following values: 5, 10, or 15.


## Project Development Reflection
### Q1. Describe how the system is personally meaningful to you.

As a student at Bowdoin College, I am continually inspired by the incredible creativity that surrounds me daily. When I first read that this project would be focused on art generation, I immediately thought of the remarkable visual art that my close friends often create. Engaging in this subject matter provided me with an excellent opportunity to develop my technical computer science skills while simultaneously celebrating and showcasing the artistic talents of one of my closest friends. There are many fair critiques that advocate against the use of generative AI in art, claiming that it diminishes genuine artistic ability. I saw this project as a way to explore how AI can be employed to elevate and display incredible, human-made art. For example, I could see dancers using a similar program to brainstorm and visualize their choreography. What made this project even more special was that I was able to collaboration with my close friend Dylan. He also mentioned that this collaboration pushed him to reflect more deeply on the art of dance. While he intuitively understood it, he had never before considered the computational aspects of how he ordered dance moves sequentially. Overall, this project was an amazing opportunity for me to learn more about my friend, and for him to engage more profoundly with his chosen art form.

### Q2. Explain how working on it genuinely challenged you as a computer scientist. How did you push yourself outside of your comfort zone? Why was this an important challenge for you?

One of the main challenges I encountered while working on this project was processing videos in Python. I had never worked with video processing in Python before, so I spent a significant portion of my time reading the documentation for the 'moviepy' library and learning how to implement it effectively. This task proved to be more demanding than I initially anticipated. Firstly, I had to ensure that I had all the necessary installations in place. Additionally, I had to ensure that the clips were the right size, were timed to display sequentially, and were aligned in a visually appealing manner. Although the learning curve was challenging, I now have a much better understandin of moviepy and I believe I could utilize it in future projects with greater ease. More generally, this project enabled me to practice adapting to new tools quickly and efficiently, which is an incredibly crucial skill in the professional field of computer science.


### Q3. What are the next steps for you going forward?

Going forward, I would want to enhance the dance model by employing smoother transitions between dance moves. While the current model provides a helpful tools for visualizing the sequential progression of dance moves, it lacks the ability to illustrate the seamless flow from one move to another. To achieve this, I could introduce more transitional dance moves and pay closer attention to the composition of the various clips. Additionally, I could improve the model by gathering transition probabilities from a broader range of dance styles and experts. Currently, the model relies on a single expert. However, dance choreography can vary significantly across different people. Therefore, incorporating a larger variety of knowledge would result in a more general dance model.

### Q4. Is your system creative?

While my system incorporates randomness and probability through the use of Markov chains, I would not say that it is highly creative. In my view, creativity entails the generation of something relatively new and unexpected, whether to youself or to the world. This model, in contrast, is entirely reliant on established dance moves and sequential trends. While there are certainly computational aspects found in all choreography (certain moves conventionally come after one another), dancers often infuse their performance with unique elements such as distinctive facial expressions, personal interpretations of moves, and other small details. This model, on the other hand, operates within a constrained framework, limited to rearranging a predefined set of input clips. While it can serve as useful tool for dancers and choreopgraphers, I do not believe that it is genuinly creative.
