import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1332, 850
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Waifu Battle")

WHITE = (255, 255, 255)
BLACK = (0,0,0)
BORDER = pygame.Rect(0, HEIGHT/2, 100000, 10)
BLOOD = (255, 0, 0)
PEE = (255, 255, 0)

MAKIMA_AUDIO = pygame.mixer.Sound(os.path.join('Assets', 'audio1.mp3'))
ASUNA_AUDIO = pygame.mixer.Sound(os.path.join('Assets', 'audio2.mp3'))



HP_FONT = pygame.font.SysFont('opensans', 40)
WINNER_FONT = pygame.font.SysFont('opensans', 100)
makima_hp = 10
asuna_hp = 10
FPS = 120
VEL = 5
BEAM_VEL = 5
MAX_BEAM = 99999999999999999999999999999999999





FIRST_HIT = pygame.USEREVENT + 1
SECOND_HIT = pygame.USEREVENT + 2

IMAGE_ONE_MAKIMA = pygame.image.load(
    os.path.join('Assets', 'makima.png'))
IMAGE_MAKIMA = pygame.transform.scale(
    IMAGE_ONE_MAKIMA, (100, 95))
IMAGE_TWO_ASUNA = pygame.image.load(
    os.path.join('Assets', 'asuna.png'))
IMAGE_ASUNA = pygame.transform.scale(
    IMAGE_TWO_ASUNA, (100, 75))

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'animebattle.jpg')), (WIDTH, HEIGHT))



def draw_window(first, second, first_beam, second_beam, makima_hp, asuna_hp):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    makima_hp_text = HP_FONT.render("HP: " +str(makima_hp), 1, PEE)
    asuna_hp_text = HP_FONT.render("HP: " +str(asuna_hp), 1, BLOOD)
    WIN.blit(makima_hp_text, (WIDTH - makima_hp_text.get_width() - 10, 10))
    WIN.blit(asuna_hp_text, (10, 10))
    WIN.blit(IMAGE_MAKIMA, (first.x, first.y))
    WIN.blit(IMAGE_ASUNA, (second.x, second.y))

    for beam in first_beam:
        pygame.draw.rect(WIN, BLOOD, beam)
    for beam in second_beam:
        pygame.draw.rect(WIN, PEE, beam)
    
    pygame.display.update()

def handle_beam(first_beam, second_beam, first, second):
    for beam in first_beam:
        beam.y += BEAM_VEL
        if second.colliderect(beam):
            pygame.event.post(pygame.event.Event(SECOND_HIT))
            first_beam.remove(beam)
        elif beam.x > HEIGHT:
            first_beam.remove(beam)
            
    
    for beam in second_beam:
        beam.y -= BEAM_VEL
        if first.colliderect(beam):
            pygame.event.post(pygame.event.Event(FIRST_HIT))
            second_beam.remove(beam)
        elif beam.x < 0:
            second_beam.remove(beam)
            
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, BLACK)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
    
    
    
    
def first_move(keys_pressed, first):
    if keys_pressed[pygame.K_a] and first.x - VEL > 0: 
        first.x -= VEL
    if keys_pressed[pygame.K_d] and first.x + VEL + first.height < WIDTH: 
        first.x += VEL  
    if keys_pressed[pygame.K_w] and first.y - VEL > 0: 
        first.y -= VEL
    if keys_pressed[pygame.K_s] and first.y + VEL + first.width < HEIGHT/2: 
        first.y += VEL 

def second_move(keys_pressed, second):
    if keys_pressed[pygame.K_LEFT] and second.x - VEL > 0: 
        second.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and second.x + VEL + second.width < WIDTH: 
        second.x += VEL  
    if keys_pressed[pygame.K_UP] and second.y - VEL > 430:  
        second.y -= VEL
    if keys_pressed[pygame.K_DOWN] and second.y + VEL + second.height < HEIGHT:  
        second.y += VEL 





def sdfusdfg():
    global makima_hp 
    global asuna_hp
    first = pygame.Rect(610, 10, 100, 95)
    second = pygame.Rect(610, 760, 100, 95)
    
    first_beam = []
    second_beam = []
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(first_beam) < MAX_BEAM:
                    beam = pygame.Rect(first.x + first.width - 50, first.y + first.height, 7, 6)
                    first_beam.append(beam)
                    MAKIMA_AUDIO.play()
                if event.key == pygame.K_RCTRL and len(second_beam) < MAX_BEAM:
                    beam = pygame.Rect(second.x + second.width - 50, second.y + second.height/2 -50, 7, 6)
                    second_beam.append(beam)
                    ASUNA_AUDIO.play()
                    
                
            if event.type == SECOND_HIT:
                    makima_hp -= 1
                    MAKIMA_AUDIO.play()
            if event.type == FIRST_HIT:  
                    asuna_hp -= 1
                    ASUNA_AUDIO.play()
                
        winner_text = ""  
        if makima_hp <= 0: 
            winner_text = "Makima won"
       
        if asuna_hp <= 0:
            winner_text = "Asuna won"
       
        if winner_text != "":
            draw_winner(winner_text)
            break
                            
              
        keys_pressed = pygame.key.get_pressed()
        first_move(keys_pressed, first)
        second_move(keys_pressed, second)
            
        handle_beam(first_beam, second_beam, first, second)    
            
               
        draw_window(first, second, first_beam, second_beam,
                    makima_hp, asuna_hp)
    sdfusdfg()


sdfusdfg()

