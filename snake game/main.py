import pygame
import random
import time


def showtext(x, y, size, message, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    textt = font.render(message, True, color)
    SCREEN.blit(textt, (x, y))


def showscore(score):
    scorex = 10
    scorey = 10
    font = pygame.font.Font('freesansbold.ttf', 30)
    textt = font.render(f"Score : {str(score)}", True, (255, 255, 255))
    SCREEN.blit(textt, (scorex, scorey))
    showtext(scorex, scorey, size=30, message=f"Score : {str(score)}", color=red)


def plotsnake(SCREEN, black, snakelist, snake_size):
    for x, y in snakelist:
        pygame.draw.rect(SCREEN, black, [x, y, snake_size, snake_size])


def welcomescreen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            maingame()
        else:
            textx = 140
            texty = 500
            showtext(textx, texty, size=30, message="PRESS SPACE OR UP KEY TO START GAME", color=red)
            showtext(670, 10, size=30, message=f"highscore = {highscore}", color=red)
            pygame.display.update()


def maingame():
    with open("C:\\Users\\LG\\PycharmProjects\\pythonProject1\\snake game\\highscore.txt", 'r+') as f:
        highscore = f.read()
    snake_x = 45
    snake_y = 55
    snake_size = 20
    move_right = False
    move_left = False
    move_up = False
    move_down = False
    find_food = True
    clock = pygame.time.Clock()
    score = 0
    snklist = []
    snklength = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    move_left = False
                    move_right = True
                    move_up = False
                    move_down = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    move_left = True
                    move_right = False
                    move_up = False
                    move_down = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    move_left = False
                    move_right = False
                    move_up = True
                    move_down = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    move_left = False
                    move_right = False
                    move_up = False
                    move_down = True
                if event.key == pygame.K_q:
                    score = score + 1
                    snklength = snklength+5
        if find_food:
            foodx = random.randint(40, SCREEN_WIDTH-40)
            foody = random.randint(40, SCREEN_HEIGHT-40)
            find_food = False

        if move_right:
            move_left = False
            snake_x = snake_x + 10
        if move_left:
            move_right = False
            snake_x = snake_x - 10
        if move_up:
            snake_y = snake_y - 10
        if move_down:
            snake_y = snake_y + 10

        if abs(snake_x-foodx) < 15 and abs(snake_y-foody) < 15:
            score = score + 1
            find_food = True
            snklength = snklength+5
        if str(score) >= highscore:
            highscore = str(score)
            with open("C:\\Users\\LG\\PycharmProjects\\pythonProject1\\snake game\\highscore.txt", 'w') as f:
                f.write(str(highscore))
        if snake_x < 0:
            snake_x = 900
        if snake_x > 900:
            snake_x = 0
        if snake_y < 0:
            snake_y = 600
        if snake_y > 600:
            snake_y = 0

        SCREEN.fill(black)
        head = list()
        head.append(snake_x)
        head.append(snake_y)
        snklist.append(head)

        if len(snklist) > snklength:

            del snklist[0]

        if head in snklist[:-1]:
            gameover(score)
            return

        plotsnake(SCREEN, (255, 255, 255), snklist, snake_size)
        pygame.draw.rect(SCREEN, (255, 0, 0), [foodx, foody, snake_size, snake_size])
        clock.tick(30)
        showscore(score)
        showtext(670, 10, size=30, message=f"highscore = {highscore}", color=red)

        pygame.display.update()


def gameover(score):
    SCREEN.fill(black)
    gameoverx = 250
    gameovery = 250
    showscore(score)

    showtext(670, 10, size=30, message=f"highscore = {highscore}", color=red)
    showtext(gameoverx, gameovery, size=60, message=f"GAME OVER!", color=red)
    pygame.display.update()

    time.sleep(2)
    SCREEN.fill(black)
    return


if __name__ == '__main__':
    black = (0, 0, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)
    pygame.init()
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    while True:
        with open("C:\\Users\\LG\\PycharmProjects\\pythonProject1\\snake game\\highscore.txt", 'r+') as f:
            highscore = f.read()
        welcomescreen()







