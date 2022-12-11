from pygame import *
init()
#классы

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_size, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed = sprite_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):

        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y < window_hight - roc1_hight:
            self.rect.y += self.speed
        if key_pressed[K_DOWN] and self.rect.y > 0:
            self.rect.y -= self.speed

class Player2(GameSprite):
     def update(self):

        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y < window_hight - roc1_hight:
            self.rect.y += self.speed
        if key_pressed[K_s] and self.rect.y > 0:
            self.rect.y -= self.speed
            

#спрайты

window_widht = 700
window_hight = 500

roc1_hight = 80
roc1_wight = 40

roc2_hight = 80
roc2_wight = 40

ball_hight = 80
ball_wight = 40

roc1_start_x = 10
roc1_start_y = window_hight / 2

roc2_start_x = 680
roc2_start_y = window_hight / 2

ball_start_x = 350
ball_start_y = 250

speed_ball_x = 3
speed_ball_y = 3

window = display.set_mode((700, 500))

#FPS

FPS = 60
clock = time.Clock()

#картинки

background = image.load('assets/pole.jpg')
background = transform.scale(background, (700, 500))

roc1_image = 'assets/rocketka.jpg'
roc2_image = 'assets/rocketka.jpg'
ball_image = 'assets/ball.jpg'



#текст

font.init()
font1 = font.Font (None, 40)
font2 = font.Font (None, 40)
win1 = font2.render('Первый игрок выиграл' , True , (255, 215,0))
win2 = font2.render('Второй игрок выиграл' , True , (255, 215,0))

#спрайты

roc1 = Player(roc1_image, roc1_start_x, roc1_start_y, (roc1_wight, roc1_hight), 10 )
roc2 = Player2(roc2_image, roc2_start_x, roc2_start_y, (roc2_wight, roc2_hight), 10 )
ball = GameSprite(ball_image, ball_start_x, ball_start_y, (ball_wight, ball_hight), 10 )

#игра

run = True
finish = False

while run:
    for i in event.get():
        if i.type == QUIT:
            run = False

    if not finish:
        roc1.update()
        roc2.update()
        ball.update()
        
        window.blit(background, (0,0))
        
        ball.rect.x += speed_ball_x
        ball.rect.y += speed_ball_y

        if ball.rect.y > window_hight - ball_hight or ball.rect.y < 0:
            speed_ball_y *= -1

        if sprite.collide_rect(ball, roc1):
            speed_ball_x *= -1

        if sprite.collide_rect(ball, roc2):
            speed_ball_x *= -1

        roc1.reset()
        roc2.reset()
        ball.reset()

        display.update()
        clock.tick(FPS)


