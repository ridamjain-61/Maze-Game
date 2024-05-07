import pygame
import sys
import font
import sound

#This file provides the UI for selection of the Theme which is asked before each level. 
#The theme is either Jurassic or Zombie with their own enemies, traps, background, sound effects, background sounds.
def select_theme(SCREEN,BG):
    ##this function is used for selecting the theme for each level.
    ##there are two themes, namely dino and zombie.
    ##there buttons for each theme with images.

    SELECT_THEME_TEXT=font.get_font(60).render("SELECT THEME", True, "#732c02")
    SELECT_THEME_RECT=SELECT_THEME_TEXT.get_rect(center=(540,100))

    DINO_THEME_TEXT=font.get_font(25).render('JURASSIC QUEST',True,"#732c02")
    DINO_THEME_RECT=DINO_THEME_TEXT.get_rect(center=(270,220))

    ZOMBIE_THEME_TEXT=font.get_font(25).render('ZOMBIE MAYHEM',True,"#732c02")
    ZOMBIE_THEME_RECT=ZOMBIE_THEME_TEXT.get_rect(center=(810,220))

    #TODO : add an image for each theme which is actually a button
    dino_theme_image=pygame.image.load('resources/dino_theme.png')
    dino_image_button_rect=pygame.Rect(30,300,480,300)

    zombie_theme_image=pygame.image.load('resources/zombie_theme.png')
    zombie_image_button_rect=pygame.Rect(570,300,480,300)
    THEME_SELECTOR=pygame.image.load('resources/wooden_interface/themeselector.png')
    
    running=True

    while running:
        SCREEN.blit(BG,(0,0))
        SCREEN.blit(SELECT_THEME_TEXT,SELECT_THEME_RECT)
        
        SCREEN.blit(THEME_SELECTOR,(15,175))
        SCREEN.blit(THEME_SELECTOR,(555,175))
        SCREEN.blit(ZOMBIE_THEME_TEXT,ZOMBIE_THEME_RECT)
        SCREEN.blit(DINO_THEME_TEXT,DINO_THEME_RECT)
        SCREEN.blit(dino_theme_image,dino_image_button_rect)
        SCREEN.blit(zombie_theme_image,zombie_image_button_rect)
        

        pygame.display.set_caption('SELECT THEME')

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if dino_image_button_rect.collidepoint(pygame.mouse.get_pos()):
                    sound.button_click_sound()
                    return 'dino'
                if zombie_image_button_rect.collidepoint(pygame.mouse.get_pos()):
                    sound.button_click_sound()
                    return 'zombie'

        pygame.display.flip()
                

        

