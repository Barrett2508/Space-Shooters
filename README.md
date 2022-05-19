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
     
 WHY I MADE SPACE SHOOTERS
 
 I am currently looking to fill my resume with awesome python projects. In addition to this Space Invaders is one of my favorite classic arcade games, and I thought it would be cool to have my very own version of it to play locally, ad-free anytime I like. The abaility to tweak the code and fully customise the code and how the game works was also something I though would be fun. 
     
HOW IT WORKS

The game works by checking for actions at a maximum rate of 60 times per second. This is because the maximum frame rate set for the game is 60 FPS so that it has greater compatability and higher consistency on all devices. Depending on the event that occured, a function will be called from a predefined corresponding class. The functions all have different outcomes which can be seen noted throughout the game.py file. 
    
If a player object collides with an enemy object (ship or laser) the enemy object will be deleted from the game to signify its destruction. Once all enemies for the wave have been defeated, the level will increase and new enemies will spawn. At the top of the window in the center the amount of enemies spawned for that level will be displayed, and the level you are on as well as lives remaining. Lives are taken when enemies pass the bottom of the window. As stated earlier in the document, from level 5 upwards players are granted 1 life per level completed.
    
Enemies are spawned out of the play-screen all in one go, and move down vertically towards the player. As mentioned earlier, the speed the enemy moves at will increase at a rate of 0.1 pixels per wave. Players are spawned in the center of the window at the bottom, and have a dynamic healthbar that depletes as the player takes damage. Once the healthbar is empty, it is game over! 
    
    
    
    
