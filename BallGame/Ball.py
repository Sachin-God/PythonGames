import pygame
import random

# defining Colors
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
light_Blue = (173, 216, 230)
orange = (255, 165, 0)

pygame.init()

# initializing Game Window
Width = 1280
Height = 720
gameWindow = pygame.display.set_mode((Width, Height))

# Setting Font
font = pygame.font.SysFont(None,40)

# Setting Application Name
pygame.display.set_caption("Ball Game")

# Setting Variable
ball_radius = 10
platformWidth = 100
platformHeight = 10
fps = 60

# Creates a clock object to control the frame rate.
clock = pygame.time.Clock()

#initializing Variables for Game
lives = 3
ballPosition = [Width//2, Height//2]
platformPosition = [Width//1.1 - platformWidth, Height//1.1 - platformHeight]
level = 1
score = 0
ballSpeed = [random.uniform(3, 6), random.uniform(3, 6)]
platformSpeed = 10
platformColor = white

def showText(text, fontSize, positionY):
    font = pygame.font.Font(None, fontSize)
    textRender = font.render(text, True, white)
    textRect = textRender.get_rect(center=(Width//2, positionY))
    gameWindow.blit(textRender, textRect) # The Pygame blit() method is one of the methods to place an image onto the screens of pygame applications. It intends to put an image on the screen. It just copies the pixels of an image from one surface to another surface just like that.

def changePlatform():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def wait_for_key(): # Waiting for Key Input
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def startScreen():
    gameWindow.fill(black)
    showText("Bouncing Ball Game", 50, Height // 4)
    showText("Press any key to start...", 30, Height // 3)
    showText("Move the platform with arrow keys...", 30, Height // 2)
    pygame.display.flip() # Flips the display to make the changes visible
    wait_for_key()

def gameOver():
    gameWindow.fill(black)
    showText("Bouncing Ball Game", 50, Height // 4)
    showText(f"GAME OVER!! your Final Score is {score}", 30, Height // 3)
    showText("Press any key to restart...", 30, Height // 2)
    pygame.display.flip() # Flips the display to make the changes visible
    wait_for_key()

startScreen()
gameRunning = True

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    keys = pygame.key.get_pressed() # Reads the state of the arrow keys

    # Platform Movement via keys Input not automatic
    platformPosition[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * platformSpeed
    platformPosition[0] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * platformSpeed

    # Platform Limitation so that it doesn't leave the display Boundaries
    platformPosition[0] = max(0, min(platformPosition[0], Width - platformWidth))
    platformPosition[1] = max(0, min(platformPosition[1], Height - platformHeight))

    # ball Movement
    ballPosition[0] += ballSpeed[0]
    ballPosition[1] += ballSpeed[1]

    # Balls Bouncing at Walls
    if ballPosition[0] <= 0 or ballPosition[0] >= Width:
        ballSpeed[0] = -ballSpeed[0]

    if ballPosition[1] <= 0:  # Only checking one condition because Platform is for bouncing, yayyy!!
        ballSpeed[1] = -ballSpeed[1]

    # ball Hitting Platform
    if (platformPosition[0] <= ballPosition[0] <= platformPosition[0] + platformWidth) and (platformPosition[1] <= ballPosition[1] <= platformPosition[1] + platformHeight):  # Ball touching platform at any position in its entire width
        ballSpeed[1] = -ballSpeed[1]
        score += 1

    # checking if Player Advancing to nextLevel
    if score >= level * 10:
        level += 1
        ballPosition = [Width//2, Height//2]
        ballSpeed = [random.uniform(3, 6), random.uniform(3, 6)]
        platformColor = changePlatform()

    # Checking if ball Fall off
    if ballPosition[1] >= Height:
        # Decrease lives
        lives -= 1
        if lives == 0:
            gameOver()
            startScreen()  # Restart the game after game over
            score = 0
            lives = 3
            current_level = 1
        else:
            # Reset the ball position
            ballPosition = [Width//2, Height//2]
            # Randomize the ball speed
            ball_speed = [random.uniform(3, 6), random.uniform(3, 6)]

        # Clear the screen
    gameWindow.fill(black)

    # Draw the ball
    pygame.draw.circle(gameWindow, white, (int(ballPosition[0]), int(ballPosition[1])), ball_radius)

    # Draw the platform
    pygame.draw.rect(gameWindow, platformColor,
                     (int(platformPosition[0]), int(platformPosition[1]), platformWidth, platformHeight))

    # Display information
    info_line_y = 10  # Adjust the vertical position as needed
    info_spacing = 75  # Adjust the spacing as needed

    # Display Score
    scoreText = font.render(f"Score: {score}", True, black)
    scoreRect = scoreText.get_rect(topleft=(10,info_line_y))
    pygame.draw.rect(gameWindow, orange, scoreRect.inflate(10, 5))
    gameWindow.blit(scoreText, scoreRect)

    # Display level
    levelText = font.render(f"level: {level}", True, white)
    levelRect = levelText.get_rect(topleft=(scoreRect.topright[0] + info_spacing, info_line_y))
    pygame.draw.rect(gameWindow, light_Blue, levelRect.inflate(10, 5))
    gameWindow.blit(levelText, levelRect)

    # Display lives
    livesText = font.render(f"lives: {lives}", True, white)
    livesRect = livesText.get_rect(topleft=(levelRect.topright[0] + info_spacing, info_line_y))
    pygame.draw.rect(gameWindow, red, livesRect.inflate(10, 5))
    gameWindow.blit(livesText, livesRect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(fps)

pygame.quit()