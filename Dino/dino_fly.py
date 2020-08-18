import pygame as py
import random


py.init()

game = True
Win = py.display.set_mode((700,400))
dino_hit = [py.image.load('dino_image\dino_duck_1.png'),py.image.load('dino_image\dino_duck_2.png'),py.image.load('dino_image\dino_hit_1.png'),py.image.load('dino_image\dino_hit_2.png')]
dino_fly = [py.image.load('dino_image/bird_1.png'),py.image.load('dino_image/bird_2.png'),py.image.load('dino_image/bird_1.png'),py.image.load('dino_image/bird_2.png')]
dino_duck = [py.image.load('dino_image\dino_duck_1.png'),py.image.load('dino_image\dino_duck_2.png'),py.image.load('dino_image\dino_duck_1.png'),py.image.load('dino_image\dino_duck_2.png')]
dino_run = [py.image.load('dino_image\dino_b_up.png'), py.image.load('dino_image\dino_f_up.png'), py.image.load('dino_image\dino_b_up.png'), py.image.load('dino_image\dino_f_up.png')]
bg = py.image.load('dino_image/bg.png')
cact = py.image.load('dino_image/obs_8.png')
USEREVENT = 0
bgx = 0
bgx2 = bg.get_width()
speed = 30
x = 100
y = 337
neg = 1
jumplist = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
clock = py.time.Clock()
py.time.set_timer(USEREVENT+1, 500)



class player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.running = True
        self.jumping = False
        self.flying = False
        self.hitting = False
        self.ducking = False
        self.runcount = 0
        self.jumpcount = 0
        self.duckcount = 0
        self.flycount = 0
        self.hitcount = 0
        self.count = 0
        self.crr = 0

    def run(self):
        if self.running == True:
            if self.runcount + 1 >160:
                self.runcount = 0
            Win.blit(dino_run[self.runcount//40], (self.x, self.y+self.crr))
            self.runcount += 1

    def duck(self):
        if self.ducking == True and self.flying == False:
            self.running = False

            if self.duckcount +1 >160:
                self.duckcount = 0
            self.crr = 20
            Win.blit(dino_duck[self.duckcount//40], (self.x, self.y+self.crr))
            self.duckcount += 1


    def fly(self):
        if self.flying == True:
            self.running = False
            self.jumping = False
            self.ducking = False

            if keys[py.K_RIGHT]:
                self.x += 2

            if keys[py.K_LEFT]:
                self.x -= 2

            if keys[py.K_UP]:
                self.y -= 2

            if keys[py.K_DOWN]:
                self.y += 2

            if self.flycount + 1 >160:
                self.flycount = 0
            if self.y > 355:
                self.y = 355
            if self.y < 0:
                self.y = 0
            if self.x > 651:
                self.x = 651
            if self.x < 0:
                self.x = 0

            Win.blit(dino_fly[self.flycount//40], (self.x, self.y+self.crr))
            self.flycount += 1




    def jump(self):
        if self.jumping == True and self.flying == False:
            self.ducking = False
            self.y -= jumplist[self.jumpcount]*1.3
            if self.y > 337:
                self.y = 337
            Win.blit(dino_run[self.jumpcount//28],(self.x, self.y+self.crr))
            self.jumpcount += 1
            if self.jumpcount > 108:
                self.jumpcount = 0
                self.jumping = False
                self.running = True

class cactus(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)
        self.img = cact
    def draw(self):
        self.hitbox = ()
        Win.blit(self.img, (self.x, self.y))
        py.draw.rect(Win,(255, 0, 0), self.hitbox,2)


dino = player(x,y)
while game:
    clock.tick(speed)
    keys = py.key.get_pressed()

    for event in py.event.get():
        if event.type == py.QUIT:
            game = False
        if event.type == USEREVENT+1:
            speed += 1

    if keys[py.K_SPACE]:
        dino.jumping = True

    if keys[py.K_f]:
        dino.flying = True


    if keys[py.K_d]:
        dino.flying = False
        dino.running = True
        dino.x = 100
        dino.y = 337

    if keys[py.K_h]:
        dino.hitting = True

    if keys[py.K_DOWN]:
        dino.ducking = True
    else:
        dino.running = True
        dino.ducking = False
        dino.crr = 0

    Win.blit(bg, (bgx, 0))
    Win.blit(bg, (bgx2, 0))
    bgx -= 1
    bgx2 -= 1
    if bgx < bg.get_width() * -1:
        bgx = bg.get_width()
    if bgx2 < bg.get_width() * -1:
        bgx2 = bg.get_width()

    dino.fly()
    dino.jump()
    dino.duck()
    dino.run()
    py.display.update()
