import pygame, string
from pygame.locals import *
import config


def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass


def display_box_(screen, message, size,position):
    fontobject = pygame.font.Font(None, 30)
    pygame.draw.rect(screen, (0, 0, 0),
                     (position[0] - size[0]/2-5,
                      position[1] - size[1]/2-5,
                      size[0]+10,size[1]+10), 0)
    pygame.draw.rect(screen, config.CYAN,
                     [position[0] - size[0] / 2,
                      position[1] - size[1] / 2,
                      size[0], size[1]], )
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (0,0,0)),
                    (position[0]-7, position[1]-8))
    pygame.display.update()


def display_box(screen, message, size):
    fontobject = pygame.font.Font(None, 30)
    pygame.draw.rect(screen, (0, 0, 0),
                     ((screen.get_width() / 2) - 100,
                      (screen.get_height() / 2) - 10,
                      200, 20), 0)
    pygame.draw.rect(screen, config.CYAN,
                     [(screen.get_width() / 2) - size[0] / 2,
                      (screen.get_height() / 2) - size[1] / 2,
                      size[0], size[1]], )
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (0,0,0)),
                    ((screen.get_width() / 2) - size[0] / 2 + 20, (screen.get_height() / 2) - size[1] / 2 + 10))
    pygame.display.update()


def ask(screen, question, size):
    pygame.font.init()
    current_string = []
    display_box(screen, question + " : " + string.join(current_string, ""), size)
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_ESCAPE:
            return None
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, question + " : " + string.join(current_string, ""), size)
    return string.join(current_string, "")

#pygame.font.init()
#screen = pygame.display.set_mode(config.screen_size)
#while True:
#    display_box_(screen,str(5),[40,40],[100,100])
