import pygame
import font
import sys
from button import Button
import screens
import sound

##This file maintains the leaderboard and extracts the data of the leaderboard present in the leaderboards folder of the parent directory. The leaderboards are updated after each game session and displayed even at the end of the game session as well as in leaderboard tab under options tab. All the three levels have their individual leaderboards.
##This has two functions. One for the leaderboard interface, and the other for the display of the leaderboard according to the level selected.
def leaderboard_interface(SCREEN,BG,music_path,music_status):
##the leaderboard interface and choosing the level
    LEADERBOARD_TEXT=font.get_font(70).render("LEADERBOARD", True, "#732c02")
    LEADERBOARD_RECT=LEADERBOARD_TEXT.get_rect(center=(540, 60))
    
    LEVEL1_BUTTON=Button(pygame.image.load("resources/wooden_interface/2.png"),(540,175),"LEVEL 1",font.get_font(35),"#93ff10","#73ff10")
    LEVEL2_BUTTON=Button(pygame.image.load("resources/wooden_interface/2.png"),(540,325),"LEVEL 2",font.get_font(35),"#93ff10","#73ff10")
    LEVEL3_BUTTON=Button(pygame.image.load("resources/wooden_interface/2.png"),(540,475),"LEVEL 3",font.get_font(35),"#93ff10","#73ff10")

    BACK_BUTTON=Button(pygame.image.load("resources/wooden_interface/2.png"),(540,625),"BACK",font.get_font(35),"#93ff10","#73ff10")
    running=True

    while running:
        SCREEN.blit(BG,(0,0))

        SCREEN.blit(LEADERBOARD_TEXT,LEADERBOARD_RECT)

        MENU_MOUSE_POS=pygame.mouse.get_pos()

        pygame.display.set_caption("LEADERBOARD")

        BACK_BUTTON.changeColor(MENU_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        LEVEL1_BUTTON.changeColor(MENU_MOUSE_POS)
        LEVEL1_BUTTON.update(SCREEN)

        LEVEL2_BUTTON.changeColor(MENU_MOUSE_POS)
        LEVEL2_BUTTON.update(SCREEN)

        LEVEL3_BUTTON.changeColor(MENU_MOUSE_POS)
        LEVEL3_BUTTON.update(SCREEN)     
 

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    screens.options(SCREEN,BG,music_path,music_status)

                if LEVEL1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    show_leaderboard(SCREEN,BG,1,music_path,music_status)

                if LEVEL2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    show_leaderboard(SCREEN,BG,2,music_path,music_status)
                
                if LEVEL3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    show_leaderboard(SCREEN,BG,3,music_path,music_status)

        pygame.display.flip()


def show_leaderboard(SCREEN,BG,level,music_path,music_status):
    ## This function is for displaying the leaderboard by calling upon text from the leaderboard file which is separate for each level. ##
    LEVEL1_TEXT=font.get_font(50).render("LEVEL 1", True, "#732c02")
    LEVEL1_RECT=LEVEL1_TEXT.get_rect(center=(540, 125))

    LEVEL2_TEXT=font.get_font(50).render("LEVEL 2", True, "#732c02")
    LEVEL2_RECT=LEVEL2_TEXT.get_rect(center=(540, 125))

    LEVEL3_TEXT=font.get_font(50).render("LEVEL 3", True, "#732c02")
    LEVEL3_RECT=LEVEL3_TEXT.get_rect(center=(540, 125))

    BACK_BUTTON=Button(pygame.image.load("resources/wooden_interface/2.png"),(540,640),"BACK",font.get_font(55),"#93ff10","#73ff10")
    LEADERBOARD_IMG=pygame.image.load('resources/wooden_interface/leaderboard.png')

    MENU_MOUSE_POS=pygame.mouse.get_pos()   
    
    if level==1:

        file1=open('leaderboards/leaderboard1.txt','r')
        names=[]
        scores=[]

        
        for line in file1:
            entries=line.strip().split(',')

            names.append(entries[0].strip())
            scores.append(entries[1].strip())

        
            


        name1=names[0]
        score1=scores[0]

        name2=names[1]
        score2=scores[1]

        name3=names[2]
        score3=scores[2]

        HIGH_SCORE_1_TEXT=font.get_font(30).render("1."+name1+" "+score1, True, "#732c02")
        HIGH_SCORE_1_RECT=HIGH_SCORE_1_TEXT.get_rect(center=(540,235))

        HIGH_SCORE_2_TEXT=font.get_font(30).render("2."+name2+" "+score2, True, "#732c02")
        HIGH_SCORE_2_RECT=HIGH_SCORE_2_TEXT.get_rect(center=(540,335))

        HIGH_SCORE_3_TEXT=font.get_font(30).render("3."+name3+" "+score3, True, "#732c02")
        HIGH_SCORE_3_RECT=HIGH_SCORE_3_TEXT.get_rect(center=(540,435))

        running=True
        while running:

            SCREEN.blit(BG,(0,0))
            SCREEN.blit(LEADERBOARD_IMG,(290,25))
            SCREEN.blit(LEVEL1_TEXT,LEVEL1_RECT)
            SCREEN.blit(HIGH_SCORE_1_TEXT,HIGH_SCORE_1_RECT)
            SCREEN.blit(HIGH_SCORE_2_TEXT,HIGH_SCORE_2_RECT)
            SCREEN.blit(HIGH_SCORE_3_TEXT,HIGH_SCORE_3_RECT)

            pygame.display.set_caption("Leaderboard Level 1")

            MENU_MOUSE_POS=pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type==pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        sound.button_click_sound()
                        leaderboard_interface(SCREEN,BG,music_path,music_status)



            BACK_BUTTON.changeColor(MENU_MOUSE_POS)
            BACK_BUTTON.update(SCREEN)

            pygame.display.flip()
 
    elif level==2:

        file1=open("leaderboards/leaderboard2.txt",'r')
        names=[]
        scores=[]
        
        
        for line in file1:
            entries=line.strip().split(',')

            names.append(entries[0].strip())
            scores.append(entries[1].strip())


        name1=names[0]
        score1=scores[0]

        name2=names[1]
        score2=scores[1]

        name3=names[2]
        score3=scores[2]

        HIGH_SCORE_1_TEXT=font.get_font(30).render("1."+name1+" "+score1, True, "#732c02")
        HIGH_SCORE_1_RECT=HIGH_SCORE_1_TEXT.get_rect(center=(540,235))

        HIGH_SCORE_2_TEXT=font.get_font(30).render("2."+name2+" "+score2, True, "#732c02")
        HIGH_SCORE_2_RECT=HIGH_SCORE_2_TEXT.get_rect(center=(540,335))

        HIGH_SCORE_3_TEXT=font.get_font(30).render("3."+name3+" "+score3, True, "#732c02")
        HIGH_SCORE_3_RECT=HIGH_SCORE_3_TEXT.get_rect(center=(540,435))
        LEADERBOARD_IMG=pygame.image.load('resources/wooden_interface/leaderboard.png')
        
        running=True
        while running:
            SCREEN.blit(BG,(0,0))
            SCREEN.blit(LEADERBOARD_IMG,(290,25))
            SCREEN.blit(LEVEL2_TEXT,LEVEL2_RECT)
            SCREEN.blit(HIGH_SCORE_1_TEXT,HIGH_SCORE_1_RECT)
            SCREEN.blit(HIGH_SCORE_2_TEXT,HIGH_SCORE_2_RECT)
            SCREEN.blit(HIGH_SCORE_3_TEXT,HIGH_SCORE_3_RECT)
            pygame.display.set_caption("Leaderboard Level 2")

            MENU_MOUSE_POS=pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type==pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        sound.button_click_sound()
                        leaderboard_interface(SCREEN,BG,music_path,music_status)



            BACK_BUTTON.changeColor(MENU_MOUSE_POS)
            BACK_BUTTON.update(SCREEN)

            pygame.display.flip()

    else:

        file1=open("leaderboards/leaderboard3.txt",'r')
        names=[]
        scores=[]
        
        
        for line in file1:
            entries=line.strip().split(',')

            names.append(entries[0].strip())
            scores.append(entries[1].strip())


        name1=names[0]
        score1=scores[0]

        name2=names[1]
        score2=scores[1]

        name3=names[2]
        score3=scores[2]

        HIGH_SCORE_1_TEXT=font.get_font(30).render("1."+name1+" "+score1, True, "#732c02")
        HIGH_SCORE_1_RECT=HIGH_SCORE_1_TEXT.get_rect(center=(540,235))

        HIGH_SCORE_2_TEXT=font.get_font(30).render("2."+name2+" "+score2, True, "#732c02")
        HIGH_SCORE_2_RECT=HIGH_SCORE_2_TEXT.get_rect(center=(540,335))

        HIGH_SCORE_3_TEXT=font.get_font(30).render("3."+name3+" "+score3, True, "#732c02")
        HIGH_SCORE_3_RECT=HIGH_SCORE_3_TEXT.get_rect(center=(540,435))
        LEADERBOARD_IMG=pygame.image.load('resources/wooden_interface/leaderboard.png')

        running=True
        while running:
            SCREEN.blit(BG,(0,0))
            SCREEN.blit(LEADERBOARD_IMG,(290,25))
            SCREEN.blit(LEVEL3_TEXT,LEVEL3_RECT)
            SCREEN.blit(HIGH_SCORE_1_TEXT,HIGH_SCORE_1_RECT)
            SCREEN.blit(HIGH_SCORE_2_TEXT,HIGH_SCORE_2_RECT)
            SCREEN.blit(HIGH_SCORE_3_TEXT,HIGH_SCORE_3_RECT)
            pygame.display.set_caption("Leaderboard Level 3")

            MENU_MOUSE_POS=pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type==pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        sound.button_click_sound()
                        leaderboard_interface(SCREEN,BG,music_path,music_status)



            BACK_BUTTON.changeColor(MENU_MOUSE_POS)
            BACK_BUTTON.update(SCREEN)

            pygame.display.flip()

#now we need a file which stores the data for all these scores and updates them timely upon completion of each gaem.

#now we need something to record names and then update the file accordingly.

