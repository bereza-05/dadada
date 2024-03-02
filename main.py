from pygame import *

window = display.set_mode((700, 500))
display.set_caption('da')
background = transform.scale(image.load('background.png'), (700, 500))

sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))

x1, y1 = 200, 300
x2, y2 = 400, 300
speed = 10
FPS = 60
clock = time.Clock()



game = True
while game:
    window.blit(background, (0, 0))
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False


    if keys[K_UP] and y2 > 5:
        y2 -= speed
    if keys[K_DOWN] and y2 < 395:
        y2 += speed
    if keys[K_LEFT] and x2 > 5:
        x2 -= speed
    if keys[K_RIGHT] and x2 < 595:
        x2 += speed

    if keys[K_w] and y1 > 5:
        y1 -= speed
    if keys[K_s] and y1 < 395:
        y1 += speed
    if keys[K_a] and x1 > 5:
        x1 -= speed
    if keys[K_d] and x1 < 595:
        x1 += speed


    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    display.update()
    clock.tick(FPS)