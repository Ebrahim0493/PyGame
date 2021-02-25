# Imports a game library that lets you use specific functions in your program.
import pygame
import random  # Import to generate random numbers.
import sys
# Initialize the pygame modules to get everything started.
pygame.init()

# The screen that will be created needs a width and a height.
screen_width = 1400
screen_height = 720
# This creates the screen and gives it the width and height.
screen = pygame.display.set_mode((screen_width, screen_height))

# This creates the player and gives it the image found in this folder (similarly with the enemy image).
player = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

# Get the width and height of the images in order to do boundary detection
image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()
print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# Store the positions of the player,enemy and prize as variables.
playerXPosition = 100
playerYPosition = 50
prizeXPosition = 700
prizeYPosition = 500

# Make the enemy start off screen and at a random y position.
enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy1_height)
enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)
enemy3XPosition = screen_width
enemy3YPosition = random.randint(2, screen_height - enemy3_height)


# This checks which key is pressed.
keyUp = False
keyDown = False
keyRight = False
keyLeft = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to
# represent real time game play.

# This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later.
while 1:
    screen.fill(0)  # Clears the screen.
    # This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    pygame.display.flip()  # This updates the screen.

    # This loops through events in the game.

    for event in pygame.event.get():
        # This event checks if the user quits the program, then if so it exits the program.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True    

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.

    if keyUp == True:
        # This makes sure that the user does not move the player above the window.
        if playerYPosition > 0:
            playerYPosition -= 1
    if keyDown == True:
        # This makes sure that the user does not move the player below the window.
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_height:
            playerXPosition += 1

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.

    # Bounding box for the player:
    playerBox = pygame.Rect(player.get_rect())
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    enemyBox1 = pygame.Rect(enemy1.get_rect())
    enemyBox1.top = enemy1YPosition
    enemyBox1.left = enemy1XPosition
    enemyBox2 = pygame.Rect(enemy2.get_rect())
    enemyBox2.bottom = enemy2YPosition
    enemyBox2.left = enemy2XPosition
    enemyBox3 = pygame.Rect(enemy3.get_rect())
    enemyBox3.top = enemy3YPosition
    enemyBox3.right = enemy3XPosition
    
    # Bounding box for the prize:
    prizeB0x = pygame.Rect(prize.get_rect())
    prizeB0x.top = prizeYPosition
    prizeB0x.right = prizeXPosition
    
    if playerBox.colliderect(enemyBox1) or playerBox.colliderect(enemyBox3) or playerBox.colliderect(enemyBox2):
     
                # Display losing status to the user:
        print("Sorry You lose!")
        pygame.quit()
        exit(0)
    
    # When the enemy is off the screen the user wins the game:
    if (enemy1XPosition < 0 - enemy1_width) or (enemy2XPosition < 0 - enemy2_width) or (enemy3XPosition < 0 - enemy3_width) or (playerBox.colliderect(prizeB0x)): 

       print("Winner winner chicken dinner")
       pygame.quit()
       exit(0)

    # Make enemy approach the player.
    enemy1XPosition -= 0.05
    enemy2XPosition -= 0.10
    enemy3XPosition -= 0.18
