import pygame
import time
from player import*
from wall import*
from map import*
from os import path
from zombie import*
import play
import create_map
img_dir = path.join(path.dirname(__file__),'img')
sound_dir = path.join(path.dirname(__file__), 'sound')
from config import*
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.mixer.init()
def text_objects(text, font):
    textSurfce = font.render(text, True, white)
    return textSurfce, textSurfce.get_rect()

def button(x, y, w, h, img1, img2, action=None,music=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        screen.blit(pygame.transform.scale(pygame.image.load(img1), [w, h]), (x, y))
        if click[0] == 1 and music != None:
            music = music+1
        if click[0] == 1 and action != None:
            action()
        clock.tick(30)
    else:
        screen.blit(pygame.transform.scale(pygame.image.load(img2), [w, h]), (x, y))
    return music
def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pause = False

def paused():

    while pause == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(pygame.transform.scale(pygame.image.load('img/map.gif'), [960, 640]), (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSuft, TextRect = text_objects('', largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        screen.blit(TextSuft, TextRect)
        button( 200, 450, 100, 60, 'img/play_hover.png', 'img/back_normal.png', unpause)
        button( 600, 450, 100, 60, 'img/quit_hover.png', 'img/quit_normal.png', game_intro)

        pygame.display.update()
        clock.tick(15)
# work with audio
def start_audio():
    pygame.mixer.music.load(path.join(sound_dir,'kiss.mp3'))
    pygame.mixer.music.play(loops =-1,start =0.0)
    pygame.mixer.music.set_volume(0.5)

def rewind_audio():
    pygame.mixer.music.rewind()

def stop_audio():
    pygame.mixer.music.stop()
def pause_audio():
    pygame.mixer.music.pause()

def unpause_audio():
    pygame.mixer.music.unpause()

def increase_audio():
    i = float(pygame.mixer.music.get_volume())
    if (i<1.0):
        pygame.mixer.music.set_volume(i+0.1)

def decrease_audio():
    i = float(pygame.mixer.music.get_volume())
    if (i>0.0):
        pygame.mixer.music.set_volume(i-0.1)


start_audio()
def game_intro():
    intro = True
    music = 0
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(pygame.transform.scale(pygame.image.load('img/map.gif'), [960, 640]),(0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 80)

        TextSuft, TextRect = text_objects('GAME MATRIX', largeText)
        TextRect.center = ((display_width / 2), 100)
        screen.blit(TextSuft, TextRect)

        button( (display_width / 2)-90, 200, 157, 72, 'img/play_hover.png', 'img/play_normal.png', play.test)
        button( (display_width / 2)-110, 300, 220, 60, 'img/credits_hover.png', 'img/credits_normal.png', create_map.test)
        button( (display_width / 2)-140, 400, 280, 70, 'img/options_normal.png', 'img/options_hover.png', None)
        button( (display_width / 2)-100, 500, 200, 80, 'img/quit_normal.png', 'img/quit_hover.png', quitgame)
        button( (display_width / 4)- 30, 220, 60, 60, 'img/connect_normal.png', 'img/connect_hover.png',None)
        if music%2 == 0:
            music = button( (display_width / 4 *3)-30, 220, 60 ,60, 'img/music_normal.png', 'img/music_hover.png', unpause_audio(),music=music)
        else:
            music = button( (display_width / 4 *3)-30, 220, 60, 60, 'img/not_music_normal.png', 'img/not_music_hover.png',pause_audio(),music=music)
        # print music
        button( (display_width / 4)- 30, 420, 60, 60, 'img/settings_normal.png', 'img/settings_hover.png',setting,None)
        button( (display_width / 4 *3)-30, 420, 60, 60, 'img/question_normal.png','img/question_hover.png',None,None)

        pygame.display.update()
        clock.tick(15)


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSuft, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    screen.blit(TextSuft, TextRect)

    pygame.display.update()
    time.sleep(2)
    main()

# setting game
def setting():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(pygame.transform.scale(pygame.image.load('img/setting.jpg'), [750, 450]), (100,100))
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSuft, TextRect = text_objects('SETTING', largeText)
        TextRect.center = ((display_width / 2), 200)
        screen.blit(TextSuft, TextRect)
        button(200, 200, 100, 60,'img/back_normal.png','img/back_hover.png', game_intro)
        largeText = pygame.font.Font('freesansbold.ttf', 40)
        TextSuft, TextRect = text_objects('VOLUME', largeText)
        TextRect.center = ((display_width / 4), 300)
        screen.blit(TextSuft, TextRect)

        button((display_width /2) , 300, 50, 50, 'img/sound_normal.png', 'img/sound_hover.png', increase_audio)

        button((display_width /2) +60, 300, 50, 50, 'img/soundoff_normal.png', 'img/soundoff_hover.png', decrease_audio)

        pygame.display.update()
        clock.tick(15)
game_intro()
main()
