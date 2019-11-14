import pygame as pg
import sys
import random

pg.init()
screen = pg.display.set_mode((1024, 580))

walkRight = [pg.image.load('right_1.png'), pg.image.load('right_2.png'), pg.image.load('right_3.png'),
             pg.image.load('right_4.png'), pg.image.load('right_5.png'),
             pg.image.load('right_6.png')]  # создаю список для ходьбы в лево

walkLeft = [pg.image.load('left_1.png'), pg.image.load('left_2.png'), pg.image.load('left_3.png'),
            pg.image.load('left_4.png'), pg.image.load('left_5.png'), pg.image.load('left_6.png')]
# список хотьбы на право


bg = pg.image.load('mexy.png')
playerStand = pg.image.load('idle.png')

clock = pg.time.Clock()

x = 50
y = 510
width = 60
height = 71
speed = 5  # скорость персонажа в px
jump = False
jumpcount = 10
left = False
right = False
anime = 0
anime_bird = 0
move = "right"
gameover = True


class recty():
    def __init__(self, width_rect, height_rect, color):
        self.x = random.randint(0, 1024)
        self.y = random.randint(0, 580)
        self.width = width_rect
        self.height = height_rect
        self.color = color

    def drawrrect(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y), 0)


def main():
    global anime


rects = []  # хранение блоков
while gameover:
    clock.tick(30)
    pg.time.delay(30)

    screen.blit(bg, (0, 0))

    level = [
        "                                                                                         ",
        " -------                                                                                 ",
        "                                                                                         ",
        "       -------                    ----------                                             ",
        "                                                                                         ",
        "                                                                                         ",
        "                                      ------                                             ",
        "                                                                                         ",
        "                                                                                         ",
        "                                                                                         ",
        "                ---                                                                      ",
        "                                                                                         ",
        "  ---                         ----------                                                 ",
        "          -----------                                                                    ",
        "    ----                   -----                                                         ",
    ]
    x_l = 0
    y_l = 45
    platform_width = 10
    platform_height = 10
    for i in level:
        for p in i:
            if p == "-":
                pf = pg.Surface((platform_width, platform_height))
                pf.fill((0, 0, 0))
                screen.blit(pf, (x_l, y_l))
            x_l += platform_width
        y_l += platform_height
        x_l = 0

    if anime + 1 >= 30:  # 30 кадров в секунду
        anime = 0  # не выходим за рамки списка (обновляем)
    if left:  # движение в лево, создаем анимацию
        screen.blit(walkLeft[anime // 5], (x, y))
        anime += 1
    elif right:
        screen.blit(walkRight[anime // 5], (x, y))
        anime += 1
    else:
        screen.blit(playerStand, (x, y))

    pg.display.flip()
    pg.display.update()

    for rect in rects:
        if len(rects) < 0:
            rect.append(recty(index))
        if len(rects) > 15:
            rect.pop

    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x > 0:
        x -= speed
        left = True
        right = False
        move = "left"  # задаем в какую сторону бежал персонаж
    elif keys[pg.K_RIGHT] and x < 1024 - width:
        x += speed
        left = False
        right = True
        move = "right"
    else:
        left = False
        right = False
        anime = 0
    if not jump:
        if keys[pg.K_SPACE]:
            jump = True
    else:
        if jumpcount >= -10:
            if jumpcount < 0:
                y += (jumpcount ** 2) // 3
            else:
                y -= (jumpcount ** 2) // 3
            jumpcount -= 1
        else:
            jump = False
            jumpcount = 10

if __name__ == "__main__":
    main()
