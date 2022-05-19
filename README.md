# Space-Shooters
A space invaders tribute coded in Pygame and Python 3.9. 


Welcome to the README document for Space-Shooters.

This game is coded in Python 3.9 using the pygame module. The game is a tribute to the classic arcade game 'Space Invaders'. In this documentation you will find information relating to everything you need to know about the Space-Shooters game, including how to get it up and running on your machine, instructions on playing the game, and details referencing the code and how it works. 

This game is object orientated and as such uses functions and classes frequently throughout. It is recommended you are farmiliar with such concepts before attempting to edit any code. This project, including my assets are open source and you are welcome to use them, but please do not monetize them without my express permission to do so. 

KNOWN BUGS

There are a couple of bugs that I am aware about and will work to fix as soon as possible, in this section I will briefly describe the bugs so you are aware:
    
      Player Hitbox is too small 
      
      The player hitbox is currently a little smaller than it should be.
      This is an easy fix and should be completed with the next commit.
      It is just a small change to the code required to extend the hitbox.
      
      
 HOW TO PLAY
 
 Controls:
 
     UP = w
     DOWN = s
     LEFT = a
     RIGHT = d
     BOOST = Hold Left Shift
     SHOOT = SPACE
     
 Rules:
 
     Players start with 100 health.
     Crashing into an enemy will remove 10 health.
     Being hit by an enemy laser will remove 10 health.
     Enemies that make it past you cost 1 life.
     You gain 1 life per level after level 5.
     Health does not count lives, if you get destroyed its game over.
     Player and Enemy speed increase by 0.1 per level.
     
 
