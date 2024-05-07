import pygame
import screens
import sys


##This file merely calls the Main Menu screen present in the screens.py file and initiates the game.
##It also takes in the music file path if provided by the user from command line. If none provided, then it takes it as default music preloaded in the resources section and played according to the theme selected.
if __name__=="__main__":
    #The implementation of music file path
    #If the music file exists, we play the music on the game otherwise the default music
    if len(sys.argv)>1:
        music_path=sys.argv[1]
    else:
        music_path='default'
    music_status='yes'
        
    pygame.init()
    SCREEN1_MAIN_MENU=pygame.display.set_mode((1080,720))
    BG_MAIN_MENU=pygame.image.load("resources/wooden_interface/backgrnd.png")
   
    screens.main_menu(SCREEN1_MAIN_MENU,BG_MAIN_MENU,music_path,music_status)

