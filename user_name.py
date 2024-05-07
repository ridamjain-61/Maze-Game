import pygame
import sys
import font
import sound
##This file asks for the Username of the player before the start of the game. 
##This helps in maintaining the Leaderboard with the names of the players.

def get_user_name(SCREEN,BG):
    user_name=''
    running=True

    GET_USER_TEXT=font.get_font(60).render("ENTER USER NAME", True, "#732c02")
    GET_USER_RECT=GET_USER_TEXT.get_rect(center=(540, 100))


    ENTER_TEXT=font.get_font(40).render("PRESS ENTER TO CONTINUE",True,"#732c02")
    ENTER_RECT=ENTER_TEXT.get_rect(center=(540,625))


    while running:

        #INPUT_SURFACE=pygame.Surface((720,100))
        #INPUT_SURFACE.fill('white')

        USER_NAME_TEXT=font.get_font(55).render(user_name, True, "#7a3504")
        USER_NAME_RECT=USER_NAME_TEXT.get_rect(center=(540,360))
        USER_PLAQUE=pygame.image.load('resources/wooden_interface/user_name_plaque.png')

        SCREEN.blit(BG,(0,0))
        #SCREEN.blit(INPUT_SURFACE,(180,300))
        SCREEN.blit(USER_PLAQUE,(120,200))
        SCREEN.blit(GET_USER_TEXT,GET_USER_RECT)
        SCREEN.blit(USER_NAME_TEXT,USER_NAME_RECT)
        SCREEN.blit(ENTER_TEXT,ENTER_RECT)

        

        pygame.display.set_caption("USER NAME")
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    sound.typing_sound()
                    return user_name
                
                elif event.key==pygame.K_BACKSPACE:
                    sound.typing_sound()
                    user_name=user_name[:-1]

                else:
                    sound.typing_sound()
                    user_name=user_name+event.unicode

        pygame.display.flip()


