# импорты
import pygame, sys, sqlite3
from pygame.locals import *
import random, time
pygame.init()


# ФПС
FPS = 60
FramePerSec = pygame.time.Clock()

# цвета
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTPURPLE = (153, 0, 153)
SHADOW = (192, 192, 192)
ORANGE = (255,100,10)
RUST = (210,150,75)
GREY = (127,127,127)
NAVY_BLUE = (0,0,100)
HIGHLIGHTER = (255,255,100)
MAGENTA = (255,0,230)
MARROON = (115,0,0)
MOON_GLOW = (235,245,255)
BLUEVIOLET = (138, 43, 226, 255)
POWDERBLUE = (176, 224, 230, 255)
PURPLEBLUE = (204, 204, 255)


# DataBase
con = sqlite3.connect("server.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS players(name, highest_score)")


# добавил всю инициализацию в функцию для рестарта игры
def init():

    global SCREEN_WIDTH, SCREEN_HEIGHT, RIGHT_PART_SPEED, LEFT_PART_SPEED, R_SPEED, L_SPEED, SCORE, COIN_SCORE, COIN_PICKED
    global LEFT_PART, RIGHT_PART, PARTS, ENEMIES, R_ENEMIES, MUSIC, PLAYING, DEAD, RESTART
    global INPUT_RECT, WRITING_NAME, USER_NAME, TOO_LONG, CHECKING_TOP
    global P, E1, E2, C, all_sprites, coins, player, enemies, Y

    # переменные для программы 
    Y = 5
    SCREEN_WIDTH = 840
    SCREEN_HEIGHT = 650
    RIGHT_PART_SPEED = [2, 3, 4]
    LEFT_PART_SPEED = [7, 8, 9, 10, 11, 12, 13, 14, 15]
    R_SPEED = random.choice(RIGHT_PART_SPEED)
    L_SPEED = random.choice(LEFT_PART_SPEED)
    SCORE = 0
    COIN_SCORE = 0
    COIN_PICKED = False
    LEFT_PART = [i for i in range(200, 391, 1)]
    RIGHT_PART = [i for i in range(450, 641, 1)]
    PARTS = LEFT_PART + RIGHT_PART
    ENEMIES = ['police.png', 'audi1.png', 'minitruck.png', 'supra1.png', 'taxi.png', 'audi2.png', 'audi3.png', 'supra2.png', 'supra3.png']
    R_ENEMIES = ['rpolice.png', 'raudi1.png', 'rminitruck.png', 'rsupra1.png', 'rtaxi.png', 'raudi2.png', 'raudi3.png', 'rsupra2.png', 'rsupra3.png']
    MUSIC = ['silent ride.mp3', 'self control.mp3', 'tokyo drift.mp3']
    PLAYING = False
    DEAD = False
    INPUT_RECT = pygame.Rect(280, 280, 263, 32)
    WRITING_NAME = False
    TOO_LONG = False
    USER_NAME = ''
    CHECKING_TOP = False
    RESTART = False



    # класс машины (встречка)
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load('images\\' + random.choice(ENEMIES))
            self.surf = pygame.Surface((45, 90))
            self.rect = self.surf.get_rect(center = (random.choice(LEFT_PART), 0))


        def move(self):
            global L_SPEED
            global SCORE
            global RESTART
            self.rect.move_ip(0, L_SPEED)
            if (self.rect.bottom > 750):
                self.image = pygame.image.load('images\\' + random.choice(ENEMIES))
                L_SPEED = random.choice(LEFT_PART_SPEED)
                SCORE += 1
                self.rect.top = 0
                self.rect.center = (random.choice(LEFT_PART), 0)
            if RESTART:
                self.image = pygame.image.load('images\\' + random.choice(ENEMIES))
                L_SPEED = random.choice(LEFT_PART_SPEED)
                SCORE += 1
                self.rect.top = 0
                self.rect.center = (random.choice(LEFT_PART), 0)
                RESTART = False



    # класс машины (в одно направление с игроком)
    class Reversed_Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__() 
            self.image = pygame.image.load('images\\' + random.choice(R_ENEMIES))
            self.surf = pygame.Surface((45, 90))
            self.rect = self.surf.get_rect(center = (random.choice(RIGHT_PART), 0))


        def move(self):
            global R_SPEED
            global SCORE
            global RESTART
            self.rect.move_ip(0, R_SPEED)
            if (self.rect.bottom > 750):
                self.image = pygame.image.load('images\\' + random.choice(R_ENEMIES))
                R_SPEED = random.choice(RIGHT_PART_SPEED)
                SCORE += 1
                self.rect.top = 0
                self.rect.center = (random.choice(RIGHT_PART), 0)
            if RESTART:
                self.image = pygame.image.load('images\\' + random.choice(R_ENEMIES))
                R_SPEED = random.choice(RIGHT_PART_SPEED)
                SCORE += 1
                self.rect.top = 0
                self.rect.center = (random.choice(RIGHT_PART), 0)
                RESTART = False



    # класс монет 
    class Coin(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("images\Coin.png")
            self.surf = pygame.Surface((25, 25))
            self.rect = self.surf.get_rect(center = (random.randint(150, 700), 0))


        def move(self):
            global COIN_PICKED
            self.rect.move_ip(0, 7)
            if (self.rect.bottom > 750):
                self.rect.top = 0
                self.rect.center = (random.randint(150, 700), 0)
            elif COIN_PICKED:
                self.rect.top = 0
                self.rect.center = (random.randint(150, 700), 0)
                COIN_PICKED = False


    # класс игрока (машина пользователя) 
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__() 
            self.image = pygame.image.load("images\Player.png")
            self.surf = pygame.Surface((50, 90))
            self.rect = self.surf.get_rect(center = (424, 600))
                    
        def move(self):
            pressed_keys = pygame.key.get_pressed()
            if self.rect.left > 140:
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5, 0)
            if self.rect.right < SCREEN_WIDTH-140:        
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5, 0)



    P = Player()
    E1 = Enemy()
    E2 = Reversed_Enemy()
    C = Coin()


    # сделал группы спрайтов для дальнейшего использования    
    enemies = pygame.sprite.Group()
    enemies.add(E1)
    enemies.add(E2)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P)
    all_sprites.add(E1)
    all_sprites.add(E2)
    all_sprites.add(C)
    coins = pygame.sprite.Group()
    coins.add(C)
    player = pygame.sprite.Group()
    player.add(P)


# вызвал функцию для инициализации всех нужных переменных
init()

# создаю экран
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
icon = pygame.image.load('images\icon.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption("Racer")

# загрузил все нужные картинки
background = pygame.image.load('images\Animated Street.png')
menu_bg = pygame.image.load('images\menu.png')
loose_img = pygame.image.load('images\over.png')
restart_img = pygame.image.load('images\\restart.png')
home_img = pygame.image.load('images\home.png')
quit_img = pygame.image.load('images\quit.png')
gameover_img = pygame.image.load('images\gameover.png')
score_img = pygame.image.load('images\score.png')
newhs_img = pygame.image.load('images\\newh.png')
cash_img = pygame.image.load('images\cash.png')
coin_score_item = pygame.image.load('images\Coin_Item.png')
rating_img = pygame.image.load('images\\rating.png')
reject_img = pygame.image.load('images\\reject.png')

# создал фонт
font = pygame.font.SysFont("Veradana", 65)
font_small = pygame.font.SysFont("Verdana", 20)


# функция для считывания рекорда и общее количество монет 
# пример реализации без использования sqlite3 или JSON, полностью продуманная с помощью локальных файлов
def HighScore_TotalCoins():
    global SCORE, COIN_SCORE
    is_record = False
    total = 0
    font = pygame.font.SysFont('Verdana', 20)

    with open('local_data\highscore.txt', 'r') as f:
        for i in f.readlines():
            if int(i) < SCORE:
                is_record = True
    if is_record:
        highscore = font.render("Highscore: " + str(SCORE), True, PURPLEBLUE)
    else:
        f = open('local_data\highscore.txt', 'r').readlines()
        highscore = font.render("Highscore: " + f[0], True, PURPLEBLUE)


    DISPLAYSURF.blit(highscore, (10, 5))

    with open('local_data\\totalcoins.txt', 'r') as f:
        for i in f.readlines():
            total = int(i) + COIN_SCORE
    
    coinfont = pygame.font.SysFont('Verdana', 30)
    cash_txt = coinfont.render(str(total), True, PURPLEBLUE)
    DISPLAYSURF.blit(cash_img, (780, 7))
    DISPLAYSURF.blit(cash_txt, (765 - (len(str(total))*15), 15))
    
    if is_record:
        f1 = open('local_data\highscore.txt', 'w')
        f1.write(str(SCORE))
        f1.close()
        DISPLAYSURF.blit(newhs_img, (265, 10))

    f2 = open('local_data\\totalcoins.txt', 'w')
    f2.write(str(total))
    f2.close()

    pygame.display.update()


# заставка главного меню
def Main_Menu():

    pygame.mixer.music.load('sounds\dead wrong.mp3')
    pygame.mixer.music.play(-1)
    DISPLAYSURF.blit(menu_bg, (0, 0))
    font = pygame.font.SysFont('timesnewroman', 20)
    inf = font.render("Welcome! Press SPACE to start...", True, GREY)
    DISPLAYSURF.blit(inf, (30, 600))


# топ 5 игроков
def Game_Rating():
    DISPLAYSURF.fill(PURPLEBLUE)
    rating_font = pygame.font.SysFont('timesnewroman', 55)
    txt = rating_font.render('TOP 5 PLAYERS:', True, WHITE)
    DISPLAYSURF.blit(txt, (225, 150))
    output_front = pygame.font.SysFont('timesnewroman', 45)
    more_txt = output_front.render('Name:           Score:', True, WHITE)
    DISPLAYSURF.blit(more_txt, (250, 220))
    global reject_button
    reject_button = DISPLAYSURF.blit(pygame.transform.scale(reject_img, (72, 72)), (750, 0))

    cnt = 1
    for i in cur.execute('SELECT * FROM players ORDER BY highest_score DESC'):
        if cnt == 6: break
        table_font = pygame.font.SysFont('timesnewroman', 35)
        names = table_font.render(f"{cnt}. {i[0]}", True, WHITE)
        DISPLAYSURF.blit(names, (215, 240 + (cnt * 50)))
        scores = table_font.render(f'{i[1]}', True, WHITE)
        DISPLAYSURF.blit(scores, (542, 240 + (cnt * 50)))
        cnt += 1


# обновление базы данных
def DB_Update():
    cur.execute(f'SELECT highest_score FROM players WHERE name = "{USER_NAME}"')
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO players VALUES('{USER_NAME}', {SCORE})")
        con.commit()    
    else:
        cur.execute(f"UPDATE players SET highest_score = '{SCORE}' WHERE name = '{USER_NAME}' AND highest_score < {SCORE}")
        con.commit()


# заставка меню после проигрыша
def Game_Loose():
    pygame.mixer_music.load('sounds\drip.mp3')
    pygame.mixer_music.play(-1)

    global restart, game_quit, to_home, rating
    DISPLAYSURF.fill(BLACK)
    game_over_bg = DISPLAYSURF.blit(loose_img, (0, 0))
    restart = DISPLAYSURF.blit(restart_img, (370, 490))
    game_quit = DISPLAYSURF.blit(quit_img, (500, 508))
    to_home = DISPLAYSURF.blit(home_img, (277, 503))
    game_over = DISPLAYSURF.blit(gameover_img, (300, 120))
    game_score = DISPLAYSURF.blit(score_img, (315 - (len(str(SCORE)) * 10), 390))
    rating = DISPLAYSURF.blit(rating_img, (20, 40))
    
    Score_txt = font.render(str(SCORE if SCORE != -1 else 0), True, PURPLEBLUE)
    DISPLAYSURF.blit(Score_txt, (505 - (len(str(SCORE)) * 10), 399))

    pygame.display.update()


# вызываю функцию главного меню сразу же после запуска программы
Main_Menu()


# основной луп
while True:
    
    for event in pygame.event.get():  
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_ESCAPE and not PLAYING and not DEAD:
            pygame.quit()
            sys.exit()

        # проверка нажатия кноки SPACE во время нахождения в главном меню
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not DEAD and not PLAYING:
            WRITING_NAME = True
    
        # радио в котором несколько классных треков :)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1 and PLAYING:
            pygame.mixer.music.load('sounds\\' + MUSIC[0])
            pygame.mixer.music.play(-1)  

        if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and PLAYING:
            pygame.mixer.music.load('sounds\\' + MUSIC[1])
            pygame.mixer.music.play(-1)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_3 and PLAYING:
            pygame.mixer.music.load('sounds\\' + MUSIC[2])
            pygame.mixer.music.play(-1)


        # проверка кликов при заставке после проигрыша
        if event.type == pygame.MOUSEBUTTONDOWN and DEAD:
            x, y = event.pos
            if restart.collidepoint(x, y):
                WRITING_NAME = True
            elif to_home.collidepoint(x, y):
                Main_Menu()
                DEAD = False
            elif game_quit.collidepoint(x, y):
                pygame.quit()
                sys.exit()
            elif rating.collidepoint(x, y):
                Game_Rating()
                CHECKING_TOP = True
                DEAD = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and CHECKING_TOP:
            x, y = event.pos
            if reject_button.collidepoint(x, y):
                CHECKING_TOP = False
                DEAD = True
                Game_Loose()

        # проверка кликов при вводе никнейма
        if event.type == pygame.KEYDOWN and WRITING_NAME:
            if event.key == pygame.K_RETURN:
                while USER_NAME[0] == ' ' and len(USER_NAME) > 1:
                    USER_NAME = USER_NAME[1:].strip()
                WRITING_NAME = False
                PLAYING = True
                pygame.mixer_music.load('sounds\carstartgarage.mp3')
                pygame.mixer_music.play()
                time.sleep(2)
                pygame.mixer_music.load('sounds\\' + random.choice(MUSIC))
                pygame.mixer_music.play(-1)
            elif event.key == pygame.K_BACKSPACE:
                USER_NAME = USER_NAME[:-1]
            elif not TOO_LONG:
                    USER_NAME += event.unicode

    # окно ввода никнейма
    if WRITING_NAME:
        DISPLAYSURF.blit(menu_bg, (0, 0))
        
        pygame.draw.rect(DISPLAYSURF, PURPLEBLUE, INPUT_RECT, 2)
        name_font = pygame.font.SysFont('timesnewroman', 20)
        text_surf = name_font.render(USER_NAME, True, (255, 255, 255))
        info_font = pygame.font.SysFont('timesnewroman', 35)
        info_text = info_font.render('ENTER YOUR NICKNAME:', True, PURPLEBLUE)

        if INPUT_RECT.w < text_surf.get_width() + 17:
            TOO_LONG = True
            error_font = pygame.font.SysFont('Aries', 30)
            error_text = error_font.render('NICKNAME IS TOO LONG!', True, RED)
            DISPLAYSURF.blit(error_text, (INPUT_RECT.x + 6, INPUT_RECT.y+45))
        else:
            TOO_LONG = False

        DISPLAYSURF.blit(info_text, (INPUT_RECT.x - 65, INPUT_RECT.y-55))
        DISPLAYSURF.blit(text_surf, (INPUT_RECT.x+5, INPUT_RECT.y+5))
        

    # если при вводе никнейма нажалась кнопка ENTER - запускается игра
    if PLAYING:

        DISPLAYSURF.blit(background, (0,Y))
        DISPLAYSURF.blit(background, (0, Y - 650))

        Y += 5
        if Y == 650:
            Y = 0

        scores = font_small.render('Score: ' + str(SCORE), True, WHITE)
        DISPLAYSURF.blit(scores, (50 - (len(str(SCORE)) * 10),10))

        
        DISPLAYSURF.blit(coin_score_item, (745, 10))

        score_c = font_small.render(str(COIN_SCORE), True, GREY)
        if COIN_SCORE < 10:
            DISPLAYSURF.blit(score_c, (763, 21))
        elif 9 < COIN_SCORE < 100:
            DISPLAYSURF.blit(score_c, (758, 21))
        else:
            DISPLAYSURF.blit(score_c, (750, 21))

        
        # цикл  который двигает спрайты
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        # подбор монет
        for coin in coins:
            for pl in player:
                if pygame.sprite.collide_rect(pl, coin):
                    COIN_SCORE += 1
                    COIN_PICKED = True
                    pygame.mixer.Sound('sounds\coin.wav').play()
                    coin.remove()

        # проверка столкновения пользователя с другой машиной
        for pl in player:
            for enemy in enemies:
                if pygame.sprite.collide_rect(pl, enemy):
                    pygame.mixer.Sound('sounds\crash.wav').play()
                    pygame.mixer_music.stop()
                    time.sleep(1)
                    Game_Loose()
                    HighScore_TotalCoins()
                    DB_Update()
                    
                    init()

                    PLAYING = False
                    DEAD = True
                    RESTART = True
                    SCORE = -1
                    COIN_SCORE = 0    

            
    pygame.display.update()
    FramePerSec.tick(FPS)