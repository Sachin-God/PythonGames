import pygame
import random

# Defining Our Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Initializing our Pygame
pygame.init()

set_height = 720
set_width = 1280
clock = pygame.time.Clock()  # Initializing our pygame clock

pygame.display.set_caption("Snake")
gameWindow = pygame.display.set_mode((set_width, set_height))

def scores(text, color, x, y):
    screenText = font.render(text,True,color)
    gameWindow.blit(screenText,[x,y])

def snake(gameWindow, color, snakeList, width, height):
    for x,y in snakeList:
        pygame.draw.rect(gameWindow, color, [x, y, width, height])

# game Specific Variables
exit_game = False
game_over = False
snakeX = 45
snakeY = 55
snakeWidth = snakeHeight = 10
fps = 60
velocityX = 0
velocityY = 0
initialVelocity = 4
foodX = random.randint(25, int(set_width/1.4))
foodY = random.randint(25, int(set_height/1.4))
score = 0

font = pygame.font.SysFont(None, 60)
# Defining a List For Snake For its Size
snakeList = []
size = 1

while not exit_game:
    if game_over:
        gameWindow.fill(white)
        scores("Game Over!", red, 500, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over == False
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:    # Handling Key During KeyPress/ KeyDown Event
                if event.key == pygame.K_RIGHT:
                    # snakeX = snakeX + 10
                    velocityX = initialVelocity
                    velocityY = 0

                if event.key == pygame.K_LEFT:
                    # snakeX = snakeX - 10
                    velocityX = -initialVelocity
                    velocityY = 0

                if event.key == pygame.K_UP:
                    # snakeY = snakeY - 10
                    velocityY = -initialVelocity
                    velocityX = 0

                if event.key == pygame.K_DOWN:
                    # snakeY = snakeY + 10
                    velocityY = initialVelocity
                    velocityX = 0

        snakeX += velocityX
        snakeY += velocityY

        # Updating Score and Relocating our Apple to a new Place after Being Eaten by the Snake
        if abs(foodX - snakeX) < 9 and abs(foodY - snakeY) < 9:  # abs = absolute Value
            score += 1
            foodX = random.randint(25, int(set_width / 1.4))
            foodY = random.randint(25, int(set_height / 1.4))
            size += 1

        # Game backGround
        gameWindow.fill(white)

        # Printing our GameScore
        scores("Score : " + str(score), green, 5, 5)

        # Snake Food
        pygame.draw.rect(gameWindow, red, [foodX, foodY, snakeWidth, snakeHeight])

        # Increasing our snake Length
        head = []
        head.append(snakeX)
        head.append(snakeY)
        snakeList.append(head)

        # Maintaining Our Snake Size
        if len(snakeList) > size:
            del snakeList[0]

        if head in snakeList[:-1]:
            game_over = True

        if snakeX < 0 or snakeX > set_width or snakeY < 0 or snakeY > set_height:
            game_over = True
        # Game Snake Rectangles
        # pygame.draw.rect(gameWindow, black, [snakeX, snakeY, snakeWidth, snakeHeight])
        snake(gameWindow, black, snakeList, snakeWidth, snakeHeight)

    # Updating Game Screen
    pygame.display.update()
    clock.tick(fps)  # Deciding FPS

pygame.quit()
quit()