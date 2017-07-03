# Snake Game!

import pygame, sys, random, time

# Initialize the pygame

check_errors  = pygame.init()
# print(pygame.init()) return a tuple (6,0)
# 6 denotes number of execution and 0 is errors

if check_errors[1]  > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

# Play surface
# set_mode expects a tuple 
# of width and height

playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!')

# Colors
red = pygame.Color(255, 0, 0) #red for gameover message
green = pygame.Color(0, 255, 0) #green for snake
black = pygame.Color(0, 0, 0) #black for score
white = pygame.Color(255, 255, 255) #white for background
brown = pygame.Color(165, 42, 42) #brown for food

# FPS controller
fpsController = pygame.time.Clock()

# Initializing variables
snakePos = [100, 50] #[x,y] should be less than screen size
snakeBody = [[100, 50],[90, 50],[80, 50]]

foodPos = [random.randrange(1, 72)* 10, random.randrange(1, 46)* 10 ]
foodSpawn = True

direction = 'RIGHT'
changeto = direction
score = 0
# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    gameOverSurface = myFont.render('GAME OVER!', True, red)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (360, 15)
    playSurface.blit(gameOverSurface, gameOverRect)
    pygame.display.flip()
    showScore(0)
    time.sleep(4)
    pygame.quit() # for pygame window
    sys.exit() # for the console exit
    
def showScore(displayPos=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score: {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if displayPos == 1:
        # while game is running
        Srect.midtop = (80, 10)
    else:
        # while game is over
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf, Srect)
    pygame.display.flip()
    
   
# Main logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
 
    # validation of direction
    # if snakes moving left it cannot instantenously move right
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
 
    # Update snake position [x,y]
    # snakes moves right increase x-position and vice versa
    # snake moves down incearse y-position and vice versa
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
   
   # Snake body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
       
    #Food Spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True
   
    #Background
    playSurface.fill(white)
            
    # drawing all the elements of the game
    # drawing the white playing surface
    
    playSurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))
    
    # checking whether snake reached end of screen x-axis limit
    # checking whether snake reached of screen y-axis limit
    
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
        
    # checking whether snake head crashed on itself
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
            
    pygame.display.flip()
    showScore()
    fpsController.tick(27)
        
            

