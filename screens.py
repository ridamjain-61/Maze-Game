import pygame
from button import Button
import font
import sys
import maze
from sprite import Sprite
import leaderboard
import sidebar
import themes
import user_name
import random
from collectibles_and_traps import Coin
from collectibles_and_traps import Gem
from collectibles_and_traps import Health
from collectibles_and_traps import Trap
from enemy import Enemy
import sound

clock=pygame.time.Clock()
FPS=120

def main_menu(SCREEN,BG,music_path,music_status):
    ##this is the main menu interface code
    PLAY_BUTTON=Button(pygame.image.load("resources/wooden_interface/1.png"),(540,240),"PLAY",font.get_font(55),"#93ff10","#73ff10")
    OPTIONS_BUTTON=Button(pygame.image.load("resources/wooden_interface/1.png"),(540,415),"OPTIONS",font.get_font(55),"#93ff10","#73ff10")
    QUIT_BUTTON=Button(pygame.image.load("resources/wooden_interface/1.png"),(540,590),"QUIT",font.get_font(55),"#93ff10","#73ff10")
    running=True
    pygame.mixer.music.load('resources\sounds\default_music_file_for_ui_screens.mp3')
    pygame.mixer.music.play(-1)
    while running:
        

        clock.tick(FPS)
        SCREEN.blit(BG,(0,0))
        
        MENU_TEXT = font.get_font(75).render("MAZE ADVENTURE", True, "#732c02")
        MENU_RECT = MENU_TEXT.get_rect(center=(540, 90))

        SCREEN.blit(MENU_TEXT,MENU_RECT)

        MENU_MOUSE_POS=pygame.mouse.get_pos()
    #this function returns the x and y coordinates of the posittion of the mouse pointer.
        
        pygame.display.set_caption("Main Menu")

        PLAY_BUTTON.changeColor(MENU_MOUSE_POS)
        PLAY_BUTTON.update(SCREEN)

        OPTIONS_BUTTON.changeColor(MENU_MOUSE_POS)
        OPTIONS_BUTTON.update(SCREEN)

        QUIT_BUTTON.changeColor(MENU_MOUSE_POS)
        QUIT_BUTTON.update(SCREEN)


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    play(SCREEN,BG,music_path,music_status)

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    options(SCREEN,BG,music_path,music_status)
                    #add option to mute the sound played on opening screen

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    #if time present, then add a check menu are you sure you want to quit.
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def play(SCREEN,BG,music_path,music_status):
    #this is the play button code. contains selection of levels, choosing themes and username
    LEVEL1_BUTTON=Button(pygame.image.load("resources/wooden_interface/2.png"),(540,175),"LEVEL 1",font.get_font(35),"#93ff10","#73ff10")
    LEVEL2_BUTTON=Button(pygame.image.load("resources/wooden_interface/2.png"),(540,325),"LEVEL 2",font.get_font(35),"#93ff10","#73ff10")
    LEVEL3_BUTTON=Button(pygame.image.load("resources/wooden_interface/2.png"),(540,475),"LEVEL 3",font.get_font(35),"#93ff10","#73ff10")

    MAIN_MENU_BUTTON=Button(pygame.image.load("resources/wooden_interface/2.png"),(540,625),"MAIN MENU",font.get_font(35),"#93ff10","#73ff10")

    username=user_name.get_user_name(SCREEN,BG)
    theme=themes.select_theme(SCREEN,BG)

    running=True
    #pygame.mixer.music.load(music_path)
    #pygame.mixer.music.play(-1)
    while running:
        
        clock.tick(FPS)
        SCREEN.blit(BG,(0,0))
        MENU_TEXT = font.get_font(70).render("SELECT LEVEL", True, "#732c02")
        MENU_RECT = MENU_TEXT.get_rect(center=(540, 60))
        SCREEN.blit(MENU_TEXT,MENU_RECT)
        pygame.display.set_caption("Select Level")
        MENU_MOUSE_POS=pygame.mouse.get_pos()


        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    main_menu(SCREEN,BG,music_path,music_status)

                if LEVEL1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    level1(SCREEN,BG,username,theme,music_path,music_status)

                if LEVEL2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    level2(SCREEN,BG,username,theme,music_path,music_status)
                    
                if LEVEL3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    level3(SCREEN,BG,username,theme,music_path,music_status)

            
        LEVEL1_BUTTON.changeColor(MENU_MOUSE_POS)
        LEVEL1_BUTTON.update(SCREEN)

        LEVEL2_BUTTON.changeColor(MENU_MOUSE_POS)
        LEVEL2_BUTTON.update(SCREEN)

        LEVEL3_BUTTON.changeColor(MENU_MOUSE_POS)
        LEVEL3_BUTTON.update(SCREEN)

        MAIN_MENU_BUTTON.changeColor(MENU_MOUSE_POS)
        MAIN_MENU_BUTTON.update(SCREEN)

        pygame.display.flip()

def options(SCREEN,BG,music_path,music_status):
    #this contains options to mute as well as to see the leaderboard
    #pygame.mixer.music.load('resources/sounds/default_music_file_for_ui_screens.mp3')
    #pygame.mixer.music.play(-1)

    #This will have show leaderboard button for each level individually
    LEADERBOARD_BUTTON=Button(pygame.image.load("resources/wooden_interface/1.png"),(540,250),"LEADERS",font.get_font(55),"#93ff10","#73ff10")
    MUTE_BUTTON=Button(pygame.image.load("resources/wooden_interface/1.png"),(540,425),"MUTE",font.get_font(55),"#93ff10","#73ff10")
    BACK_BUTTON=Button(pygame.image.load("resources/wooden_interface/1.png"),(540,600),"BACK",font.get_font(55),"#93ff10","#73ff10")
    #CHANGE_THEME_BUTTON=Button(pygame.image.load("resources/wooden_interface/1.png"),(540,425),"THEMES",font.get_font(65),"#93ff10","#73ff10")
    
    OPTIONS_TEXT=font.get_font(75).render("OPTIONS", True, "#732c02")
    OPTIONS_RECT=OPTIONS_TEXT.get_rect(center=(540, 90))
    
    
    running=True
    while running:
        SCREEN.blit(BG,(0,0))

        MENU_MOUSE_POS=pygame.mouse.get_pos()
        pygame.display.set_caption("OPTIONS")
        
        SCREEN.blit(OPTIONS_TEXT,OPTIONS_RECT)

        LEADERBOARD_BUTTON.changeColor(MENU_MOUSE_POS)
        LEADERBOARD_BUTTON.update(SCREEN)

        BACK_BUTTON.changeColor(MENU_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        MUTE_BUTTON.changeColor(MENU_MOUSE_POS)
        MUTE_BUTTON.update(SCREEN)


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.quit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                
                if MUTE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if music_status=='yes':
                        sound.sound_off()
                        music_status='no'
                    elif music_status=='no':
                        sound.sound_on()
                        music_status='yes'
                
                if LEADERBOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    leaderboard.leaderboard_interface(SCREEN,BG,music_path,music_status)

                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    main_menu(SCREEN,BG,music_path,music_status)

                
                    #print(music_status)
                #if CHANGE_THEME_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #themes.set_theme()

        pygame.display.flip()

def level1(SCREEN,BG,username,theme,music_path,music_status):
    #on screen 1 finally everything is displayed
    #surface 1 contains the whole maze which may be bigger than the screen as per level
    #we will slice this surface as subsurface1 and then blit it on the screen1
    #partial_rect=pygame.Rect(0,0,722,722)
    #partial_surface=SCREEN1.subsurface(partial_rect)

    ##if the musicstatus is no bgm will be played
    if music_status=='yes':
        if music_path=='default':
            if theme=='dino':
                pygame.mixer.music.load('resources/sounds/dino_theme_bgm.mp3')
                pygame.mixer.music.play(-1)
                #pygame.mixer.music.stop()
                #play dino theme default music
            else:
                pygame.mixer.music.load('resources/sounds/zombie_theme_bgm.mp3')
                pygame.mixer.music.play(-1)
                #play zombie theme default music
        
        else:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)

    elif music_status=='no':
        pygame.mixer.music.stop()

    SCREEN1=pygame.display.set_mode((1080,722))
    SURFACE1=pygame.Surface((722,722))
    maze_size=722
    tile_size=60
    rows=maze_size//tile_size
    cols=maze_size//tile_size
    side_bar_rect=pygame.Rect(722,0,358,722)
    game_screen_rect=pygame.Rect(0,0,722,722)
    #this is for generating the maze by dfs algorithm
    maze1=maze.Maze(cols,rows)
    maze1.generate_maze()
    #this is for generating our main_character_sprite
    my_sprite=Sprite(10,10,rows,cols,tile_size,theme)
    all_sprites=pygame.sprite.Group()
    all_sprites.add(my_sprite)
    #creating groups for all our collectibles
    all_coins=pygame.sprite.Group()
    all_gems=pygame.sprite.Group()
    all_health=pygame.sprite.Group()
    all_traps=pygame.sprite.Group()
    all_enemies=pygame.sprite.Group()

    #this is for generating random cells for placing our collectibles.
    c=30
    random_cells1=random.sample(maze1.grid_cells,c)
    for i in range(c):
        x=random_cells1[i].x*tile_size+tile_size/4
        y=random_cells1[i].y*tile_size+tile_size/4
        newCoin=Coin(x,y)
        all_coins.add(newCoin)
    g=6
    random_cells2=random.sample(maze1.grid_cells,g)
    for i in range(g):
        x=random_cells2[i].x*tile_size+tile_size/4
        y=random_cells2[i].y*tile_size+tile_size/4
        newGem=Gem(x,y)
        all_gems.add(newGem)
    h=10
    random_cells3=random.sample(maze1.grid_cells,h)
    for i in range(h):
        x=random_cells3[i].x*tile_size+tile_size/4
        y=random_cells3[i].y*tile_size+tile_size/4
        newHealth=Health(x,y)
        all_health.add(newHealth)
    f=10
    random_cells4=random.sample(maze1.grid_cells,f)
    for i in range(f):
        x=random_cells4[i].x*tile_size+tile_size/4
        y=random_cells4[i].y*tile_size+tile_size/4
        newTrap=Trap(x,y,theme)
        all_traps.add(newTrap)
    e=5
    random_cells5=random.sample(maze1.grid_cells,e)
    for i in range(e):
        x=random_cells5[i].x*tile_size+tile_size/4
        y=random_cells5[i].y*tile_size+tile_size/4
        newEnemy=Enemy(x,y,rows,cols,tile_size,theme)
        all_enemies.add(newEnemy)
    
    # all the counters for implementing game scores and other things.
    coin_counter=0
    gem_counter=0
    health_counter=0
    trap_counter=0
    sprite_health=200 #this is the maximum health of a sprite you cannot have more than that.
    
    start_time=pygame.time.get_ticks()
    last_speed_update=start_time
    #entering the main game loop.
    running=True
    while running:
        clock.tick(FPS)
        # CHANGE THE BACKGROUNDS ACCORDING TO RESPECTIVE THEMES
        if theme=='dino':
            BG1=pygame.image.load("resources/forest.png")
            PADDING_BG=pygame.image.load("resources/dino_theme_padding.png")
            SURFACE1.blit(BG1,(0,0))
            ENDPOINT=pygame.image.load('resources/endpoint.png')
            SURFACE1.blit(ENDPOINT,(maze_size-50,maze_size-50))
            SCREEN1.blit(PADDING_BG,(0,0))
            SCREEN1.fill(pygame.Color("#322001"),side_bar_rect)
        
        if theme=='zombie':
            BG1=pygame.image.load("resources/zombie_wallpaper.png")
            PADDING_BG=pygame.image.load("resources/zombie_padding.png")
            SURFACE1.blit(BG1,(0,0))
            ENDPOINT=pygame.image.load('resources/endpoint.png')
            SURFACE1.blit(ENDPOINT,(maze_size-50,maze_size-50))
            SCREEN1.blit(PADDING_BG,(0,0))
            SCREEN1.fill(pygame.Color("#322001"),side_bar_rect)
        
        pygame.display.set_caption("LEVEL 1")

        total_time=180
        current_time=pygame.time.get_ticks()
        elapsed_time=(current_time-start_time)//1000
        display_time=total_time-elapsed_time
        display_time=str(display_time)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                my_sprite.left_pressed=True
            if event.key==pygame.K_RIGHT:
                my_sprite.right_pressed=True
            if event.key==pygame.K_UP:
                my_sprite.up_pressed=True
            if event.key==pygame.K_DOWN:
                my_sprite.down_pressed=True
            my_sprite.check_move(tile_size,maze1.grid_cells,maze1.thickness)
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                my_sprite.left_pressed=False
            if event.key==pygame.K_RIGHT:
                my_sprite.right_pressed=False
            if event.key==pygame.K_UP:
                my_sprite.up_pressed=False
            if event.key==pygame.K_DOWN:
                my_sprite.down_pressed=False
            my_sprite.check_move(tile_size,maze1.grid_cells,maze1.thickness)

        ##stimulating the enemy randomly

        keys_choice=['leftdown','rightdown','updown','downdown','leftup','rightup','upup','downup']
        
        for random_enemy in all_enemies:

            random_key=random.choice(keys_choice)

            if random_key=='leftdown':
                random_enemy.left_pressed=True

            if random_key=='rightdown':
                random_enemy.right_pressed=True

            if random_key=='updown':
                random_enemy.up_pressed=True

            if random_key=='downdown':
                random_enemy.down_pressed=True

            if random_key=='leftup':
                random_enemy.left_pressed=False

            if random_key=='rightup':
                random_enemy.right_pressed=False

            if random_key=='upup':
                random_enemy.up_pressed=False

            if random_key=='downup':
                random_enemy.down_pressed=False

    #drawing collectibles cells and everything else on the map and updating them.
        [cell.draw(SURFACE1,tile_size) for cell in maze1.grid_cells]
        all_coins.draw(SURFACE1)
        all_coins.update()

        all_gems.draw(SURFACE1)
        all_gems.update()

        all_health.draw(SURFACE1)
        all_health.update()

        all_traps.draw(SURFACE1)
        all_traps.update()
        
        all_sprites.draw(SURFACE1)
        all_sprites.update()

        all_enemies.draw(SURFACE1)
        all_enemies.update()
##implementing collisions for each of them
        collisions_coins=pygame.sprite.spritecollide(my_sprite,all_coins,True)
        for coin in collisions_coins:
            sound.coin_sound()
            coin_counter+=1
            
        
##implemented speed increase on encountering the gem
        collisions_gems=pygame.sprite.spritecollide(my_sprite,all_gems,True)
        for gem in collisions_gems:
            sound.gem_sound()
            gem_counter+=1
            my_sprite.speed=20
            last_speed_update=pygame.time.get_ticks()

        if pygame.time.get_ticks()-last_speed_update>5000:
            my_sprite.speed=10
            
        
            
##implemented health increase on encountering the health.
        collisions_health=pygame.sprite.spritecollide(my_sprite,all_health,True)
        for health in collisions_health:
            sound.health_sound()
            if sprite_health>=200:
                sprite_health=sprite_health
            elif sprite_health<200 and sprite_health>190:
                sprite_health=200
            else:
                sprite_health+=10
                

        collisions_traps=pygame.sprite.spritecollide(my_sprite,all_traps,False)
        for trap in collisions_traps:
            sound.trap_sound(theme)
            sprite_health-=2
            if sprite_health<=0:
                pygame.mixer.music.stop()
                gameover_lost(SCREEN,BG,'health',music_path,1)


        collisions_enemy=pygame.sprite.spritecollide(my_sprite,all_enemies,False)
        for enemies in collisions_enemy:
            sound.enemy_sound(theme)
            sprite_health-=2
            if sprite_health<=0:
                pygame.mixer.music.stop()
                gameover_lost(SCREEN,BG,'health',music_path,1)


    #furthur is camera implementation
    #camera will show us screen 2.
    #screen 2 is player.x-100 to player.x+100 and player.y-100 to player.y+100
    #when player is close to boundaries, we fix the display.
        
        curr_x=my_sprite.x
        curr_y=my_sprite.y
        width=361
        
        if curr_x<=width/2 and curr_y<=width/2:
            game_display_rect=pygame.Rect(0,0,width,width)

        elif curr_x+width/2>=maze_size and curr_y+width/2>=maze_size:
            game_display_rect=pygame.Rect(maze_size-width,maze_size-width,width,width)

        elif curr_x+width/2>=maze_size and curr_y<=width/2:
            game_display_rect=pygame.Rect(maze_size-width,0,width,width)

        elif curr_x<=width/2 and curr_y+width/2>=maze_size:
            game_display_rect=pygame.Rect(0,maze_size-width,width,width)

        elif curr_x<=width/2:
            game_display_rect=pygame.Rect(0,curr_y-width/2,width,width)

        elif curr_y<=width/2:
            game_display_rect=pygame.Rect(curr_x-width/2,0,width,width)

        elif curr_y+width/2>=maze_size:
            game_display_rect=pygame.Rect(curr_x-width/2,maze_size-width,width,width)

        elif curr_x+width/2>=maze_size:
            game_display_rect=pygame.Rect(maze_size-width,curr_y-width/2,width,width)

        else:
            game_display_rect=pygame.Rect(curr_x-width/2,curr_y-width/2,width,width)
##the not so complex formula for score calculation
        score=int(((curr_x+curr_y)//5)*(elapsed_time/total_time)*(elapsed_time/total_time)+sprite_health*2*(elapsed_time/total_time)*(elapsed_time/total_time)+gem_counter*50+coin_counter*20+(total_time-elapsed_time)*10*(elapsed_time/total_time)*(elapsed_time/total_time))
        score=str(score)
        
        SUBSURFACE1=SURFACE1.subsurface(game_display_rect)
        SCREEN1.blit(SUBSURFACE1,(361/2,361/2))
        
##now checking if game is over and updatting the leaderboard.
        
        if my_sprite.isGameOver():
            #before going to gameover screen we need to see the file which contains the leaderboard and add the score accordingly if needed and then that will get displayed in the gameover screen.
            
            file=open('leaderboards/leaderboard1.txt','r')
            names=[]
            scores=[]
            for line in file:
                entries=line.strip().split(',')

                names.append(entries[0].strip())
                scores.append(entries[1].strip())

            if int(score)>=int(scores[0]):
                scores[2]=scores[1]
                scores[1]=scores[0]
                scores[0]=score

                names[2]=names[1]
                names[1]=names[0]
                names[0]=username

            elif int(score)>=int(scores[1]):
                scores[0]=scores[0]
                scores[2]=scores[1]
                scores[1]=score

                names[0]=names[0]
                names[2]=names[1]
                names[1]=username

            elif int(score)>=int(scores[2]):
                scores[0]=scores[0]
                scores[1]=scores[1]
                scores[2]=score

                names[0]=names[0]
                names[1]=names[1]
                names[2]=username

            else:
                scores=scores
                names=names

            file.close()

            with open("leaderboards/leaderboard1.txt",'w') as file:
                file.write(names[0]+','+scores[0]+'\n')
                file.write(names[1]+','+scores[1]+'\n')
                file.write(names[2]+','+scores[2]+'\n')


            #now that we have our updated our leaderboard according to the current scorecard,
            #we will write that in our leaderboard1.txt file.


                ##add health to sidebar.
                ##add lost of health in gameover_lost

            pygame.mixer.music.stop()
            gameover(SCREEN,BG,score,music_path,1)

        if int(display_time)<0:
            pygame.mixer.music.stop()
            gameover_lost(SCREEN,BG,'time',music_path,1)
        BG_SIDE=pygame.image.load('resources/BG_SIDE.png')
        SCREEN1.blit(BG_SIDE,(722,0))
        sidebar.sidebar_text(SCREEN1,score,display_time,sprite_health)
        pygame.display.flip()

def level2(SCREEN,BG,username,theme,music_path,music_status):

    #on screen 1 finally everything is displayed
    #surface 1 contains the whole maze which may be bigger than the screen as per level
    #we will slice this surface as subsurface1 and then blit it on the screen1
    #partial_rect=pygame.Rect(0,0,722,722)
    #partial_surface=SCREEN1.subsurface(partial_rect)

    if music_status=='yes':
        if music_path=='default':
            if theme=='dino':
                pygame.mixer.music.load('resources/sounds/dino_theme_bgm.mp3')
                pygame.mixer.music.play(-1)
                #pygame.mixer.music.stop()
                #play dino theme default music
            else:
                pygame.mixer.music.load('resources/sounds/zombie_theme_bgm.mp3')
                pygame.mixer.music.play(-1)
                #play zombie theme default music
        
        else:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)

    elif music_status=='no':
        pygame.mixer.music.stop()
    
    SCREEN1=pygame.display.set_mode((1080,722))
    SURFACE1=pygame.Surface((842,842))
    maze_size=842
    tile_size=50
    rows=maze_size//tile_size
    cols=maze_size//tile_size
    side_bar_rect=pygame.Rect(722,0,358,722)
    game_screen_rect=pygame.Rect(0,0,722,722)
    #this is for generating the maze by dfs algorithm
    maze1=maze.Maze(cols,rows)
    maze1.generate_maze()
    #this is for generating our main_character_sprite
    my_sprite=Sprite(10,10,rows,cols,tile_size,theme)
    all_sprites=pygame.sprite.Group()
    all_sprites.add(my_sprite)
    #creating groups for all our collectibles
    all_coins=pygame.sprite.Group()
    all_gems=pygame.sprite.Group()
    all_health=pygame.sprite.Group()
    all_traps=pygame.sprite.Group()
    all_enemies=pygame.sprite.Group()

    #this is for generating random cells for placing our collectibles.
    c=40
    random_cells1=random.sample(maze1.grid_cells,c)
    for i in range(c):
        x=random_cells1[i].x*tile_size+tile_size/4
        y=random_cells1[i].y*tile_size+tile_size/4
        newCoin=Coin(x,y)
        all_coins.add(newCoin)
    g=7
    random_cells2=random.sample(maze1.grid_cells,g)
    for i in range(g):
        x=random_cells2[i].x*tile_size+tile_size/4
        y=random_cells2[i].y*tile_size+tile_size/4
        newGem=Gem(x,y)
        all_gems.add(newGem)
    h=20
    random_cells3=random.sample(maze1.grid_cells,h)
    for i in range(h):
        x=random_cells3[i].x*tile_size+tile_size/4
        y=random_cells3[i].y*tile_size+tile_size/4
        newHealth=Health(x,y)
        all_health.add(newHealth)
    f=20
    random_cells4=random.sample(maze1.grid_cells,f)
    for i in range(f):
        x=random_cells4[i].x*tile_size+tile_size/4
        y=random_cells4[i].y*tile_size+tile_size/4
        newTrap=Trap(x,y,theme)
        all_traps.add(newTrap)
    e=12
    random_cells5=random.sample(maze1.grid_cells,e)
    for i in range(e):
        x=random_cells5[i].x*tile_size+tile_size/4
        y=random_cells5[i].y*tile_size+tile_size/4
        newEnemy=Enemy(x,y,rows,cols,tile_size,theme)
        all_enemies.add(newEnemy)
    
    # all the counters for implementing game scores and other things.
    coin_counter=0
    gem_counter=0
    health_counter=0
    trap_counter=0
    sprite_health=200 #this is the maximum health of a sprite you cannot have more than that.

    start_time=pygame.time.get_ticks()
    last_speed_update=start_time
    #entering the main game loop.
    running=True
    while running:
        clock.tick(FPS)
        #TODO : CHANGE THE BACKGROUNDS ACCORDING TO RESPECTIVE THEMES
        if theme=='dino':
            BG1=pygame.image.load("resources/forest.png")
            PADDING_BG=pygame.image.load("resources/dino_theme_padding.png")
            SURFACE1.blit(BG1,(0,0))
            ENDPOINT=pygame.image.load('resources/endpoint.png')
            SURFACE1.blit(ENDPOINT,(maze_size-50,maze_size-50))
            SCREEN1.blit(PADDING_BG,(0,0))
            SCREEN1.fill(pygame.Color("#322001"),side_bar_rect)
        
        if theme=='zombie':
            BG1=pygame.image.load("resources/zombie_wallpaper.png")
            PADDING_BG=pygame.image.load("resources/zombie_padding.png")
            SURFACE1.blit(BG1,(0,0))
            ENDPOINT=pygame.image.load('resources/endpoint.png')
            SURFACE1.blit(ENDPOINT,(maze_size-50,maze_size-50))
            SCREEN1.blit(PADDING_BG,(0,0))
            SCREEN1.fill(pygame.Color("#322001"),side_bar_rect)

        pygame.display.set_caption("LEVEL 2")

        total_time=200
        current_time=pygame.time.get_ticks()
        elapsed_time=(current_time-start_time)//1000
        display_time=total_time-elapsed_time
        display_time=str(display_time)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                my_sprite.left_pressed=True
            if event.key==pygame.K_RIGHT:
                my_sprite.right_pressed=True
            if event.key==pygame.K_UP:
                my_sprite.up_pressed=True
            if event.key==pygame.K_DOWN:
                my_sprite.down_pressed=True
            my_sprite.check_move(tile_size,maze1.grid_cells,maze1.thickness)
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                my_sprite.left_pressed=False
            if event.key==pygame.K_RIGHT:
                my_sprite.right_pressed=False
            if event.key==pygame.K_UP:
                my_sprite.up_pressed=False
            if event.key==pygame.K_DOWN:
                my_sprite.down_pressed=False
            my_sprite.check_move(tile_size,maze1.grid_cells,maze1.thickness)

        ##stimulating the enemy randomly

        keys_choice=['leftdown','rightdown','updown','downdown','leftup','rightup','upup','downup']
        
        for random_enemy in all_enemies:

            random_key=random.choice(keys_choice)

            if random_key=='leftdown':
                random_enemy.left_pressed=True

            if random_key=='rightdown':
                random_enemy.right_pressed=True

            if random_key=='updown':
                random_enemy.up_pressed=True

            if random_key=='downdown':
                random_enemy.down_pressed=True

            if random_key=='leftup':
                random_enemy.left_pressed=False

            if random_key=='rightup':
                random_enemy.right_pressed=False

            if random_key=='upup':
                random_enemy.up_pressed=False

            if random_key=='downup':
                random_enemy.down_pressed=False

    #drawing collectibles cells and everything else on the map and updating them.
        [cell.draw(SURFACE1,tile_size) for cell in maze1.grid_cells]
        all_coins.draw(SURFACE1)
        all_coins.update()

        all_gems.draw(SURFACE1)
        all_gems.update()

        all_health.draw(SURFACE1)
        all_health.update()

        all_traps.draw(SURFACE1)
        all_traps.update()
        
        all_sprites.draw(SURFACE1)
        all_sprites.update()

        all_enemies.draw(SURFACE1)
        all_enemies.update()

        collisions_coins=pygame.sprite.spritecollide(my_sprite,all_coins,True)
        for coin in collisions_coins:
            sound.coin_sound()
            coin_counter+=1
            print(coin_counter)


        collisions_gems=pygame.sprite.spritecollide(my_sprite,all_gems,True)
        for gem in collisions_gems:
            sound.gem_sound()
            gem_counter+=1
            my_sprite.speed=20
            last_speed_update=pygame.time.get_ticks()

        if pygame.time.get_ticks()-last_speed_update>5000:
            my_sprite.speed=10
            

        collisions_health=pygame.sprite.spritecollide(my_sprite,all_health,True)
        for health in collisions_health:
            sound.health_sound()
            if sprite_health>=200:
                sprite_health=sprite_health
            elif sprite_health<200 and sprite_health>190:
                sprite_health=200
            else:
                sprite_health+=10
                

        collisions_traps=pygame.sprite.spritecollide(my_sprite,all_traps,False)
        for trap in collisions_traps:
            sound.trap_sound(theme)
            sprite_health-=3
            if sprite_health<=0:
                pygame.mixer.music.stop()
                gameover_lost(SCREEN,BG,'health',music_path,2)


        collisions_enemy=pygame.sprite.spritecollide(my_sprite,all_enemies,False)
        for enemies in collisions_enemy:
            sound.enemy_sound(theme)
            sprite_health-=3
            if sprite_health<=0:
                pygame.mixer.music.stop()
                gameover_lost(SCREEN,BG,'health',music_path,2)


    #furthur is camera implementation
    #camera will show us screen 2.
    #screen 2 is player.x-100 to player.x+100 and player.y-100 to player.y+100
    #when player is close to boundaries, we fix the display.
        
        curr_x=my_sprite.x
        curr_y=my_sprite.y
        width=361
        
        if curr_x<=width/2 and curr_y<=width/2:
            game_display_rect=pygame.Rect(0,0,width,width)

        elif curr_x+width/2>=maze_size and curr_y+width/2>=maze_size:
            game_display_rect=pygame.Rect(maze_size-width,maze_size-width,width,width)

        elif curr_x+width/2>=maze_size and curr_y<=width/2:
            game_display_rect=pygame.Rect(maze_size-width,0,width,width)

        elif curr_x<=width/2 and curr_y+width/2>=maze_size:
            game_display_rect=pygame.Rect(0,maze_size-width,width,width)

        elif curr_x<=width/2:
            game_display_rect=pygame.Rect(0,curr_y-width/2,width,width)

        elif curr_y<=width/2:
            game_display_rect=pygame.Rect(curr_x-width/2,0,width,width)

        elif curr_y+width/2>=maze_size:
            game_display_rect=pygame.Rect(curr_x-width/2,maze_size-width,width,width)

        elif curr_x+width/2>=maze_size:
            game_display_rect=pygame.Rect(maze_size-width,curr_y-width/2,width,width)

        else:
            game_display_rect=pygame.Rect(curr_x-width/2,curr_y-width/2,width,width)

        score=int(((curr_x+curr_y)//5)*(elapsed_time/total_time)*(elapsed_time/total_time)+sprite_health*2*(elapsed_time/total_time)*(elapsed_time/total_time)+gem_counter*50+coin_counter*20+(total_time-elapsed_time)*10*(elapsed_time/total_time)*(elapsed_time/total_time))
        score=str(score)
        
        SUBSURFACE1=SURFACE1.subsurface(game_display_rect)
        SCREEN1.blit(SUBSURFACE1,(361/2,361/2))


        if my_sprite.isGameOver():
            #before going to gameover screen we need to see the file which contains the leaderboard and add the score accordingly if needed and then that will get displayed in the gameover screen.
            
            file=open('leaderboards/leaderboard2.txt','r')
            names=[]
            scores=[]
            for line in file:
                entries=line.strip().split(',')

                names.append(entries[0].strip())
                scores.append(entries[1].strip())

            if int(score)>=int(scores[0]):
                scores[2]=scores[1]
                scores[1]=scores[0]
                scores[0]=score

                names[2]=names[1]
                names[1]=names[0]
                names[0]=username

            elif int(score)>=int(scores[1]):
                scores[0]=scores[0]
                scores[2]=scores[1]
                scores[1]=score

                names[0]=names[0]
                names[2]=names[1]
                names[1]=username

            elif int(score)>=int(scores[2]):
                scores[0]=scores[0]
                scores[1]=scores[1]
                scores[2]=score

                names[0]=names[0]
                names[1]=names[1]
                names[2]=username

            else:
                scores=scores
                names=names

            file.close()

            with open("leaderboards/leaderboard2.txt",'w') as file:
                file.write(names[0]+','+scores[0]+'\n')
                file.write(names[1]+','+scores[1]+'\n')
                file.write(names[2]+','+scores[2]+'\n')


            #now that we have our updated our leaderboard according to the current scorecard,
            #we will write that in our leaderboard1.txt file.


                ##add health to sidebar.
                ##add lost of health in gameover_lost

            pygame.mixer.music.stop()
            gameover(SCREEN,BG,score,music_path,2)

        if int(display_time)<0:
            pygame.mixer.music.stop()
            gameover_lost(SCREEN,BG,'time',music_path,2)
        BG_SIDE=pygame.image.load('resources/BG_SIDE.png')
        SCREEN1.blit(BG_SIDE,(722,0))
        sidebar.sidebar_text(SCREEN1,score,display_time,sprite_health)
        pygame.display.flip()

def level3(SCREEN,BG,username,theme,music_path,music_status):
    #on screen 1 finally everything is displayed
    #surface 1 contains the whole maze which may be bigger than the screen as per level
    #we will slice this surface as subsurface1 and then blit it on the screen1
    #partial_rect=pygame.Rect(0,0,722,722)
    #partial_surface=SCREEN1.subsurface(partial_rect)

    if music_status=='yes':
        if music_path=='default':
            if theme=='dino':
                pygame.mixer.music.load('resources/sounds/dino_theme_bgm.mp3')
                pygame.mixer.music.play(-1)
                #pygame.mixer.music.stop()
                #play dino theme default music
            else:
                pygame.mixer.music.load('resources/sounds/zombie_theme_bgm.mp3')
                pygame.mixer.music.play(-1)
                #play zombie theme default music
        
        else:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)

    elif music_status=='no':
        pygame.mixer.music.stop()
    
    SCREEN1=pygame.display.set_mode((1080,722))
    SURFACE1=pygame.Surface((1080,1080))
    maze_size=1080
    tile_size=50
    rows=maze_size//tile_size
    cols=maze_size//tile_size
    side_bar_rect=pygame.Rect(722,0,358,722)
    game_screen_rect=pygame.Rect(0,0,722,722)
    #this is for generating the maze by dfs algorithm
    maze1=maze.Maze(cols,rows)
    maze1.generate_maze()
    #this is for generating our main_character_sprite
    my_sprite=Sprite(10,10,rows,cols,tile_size,theme)
    all_sprites=pygame.sprite.Group()
    all_sprites.add(my_sprite)
    #creating groups for all our collectibles
    all_coins=pygame.sprite.Group()
    all_gems=pygame.sprite.Group()
    all_health=pygame.sprite.Group()
    all_traps=pygame.sprite.Group()
    all_enemies=pygame.sprite.Group()

    #this is for generating random cells for placing our collectibles.
    c=60
    random_cells1=random.sample(maze1.grid_cells,c)
    for i in range(c):
        x=random_cells1[i].x*tile_size+tile_size/4
        y=random_cells1[i].y*tile_size+tile_size/4
        newCoin=Coin(x,y)
        all_coins.add(newCoin)
    g=15
    random_cells2=random.sample(maze1.grid_cells,g)
    for i in range(g):
        x=random_cells2[i].x*tile_size+tile_size/4
        y=random_cells2[i].y*tile_size+tile_size/4
        newGem=Gem(x,y)
        all_gems.add(newGem)
    h=30
    random_cells3=random.sample(maze1.grid_cells,h)
    for i in range(h):
        x=random_cells3[i].x*tile_size+tile_size/4
        y=random_cells3[i].y*tile_size+tile_size/4
        newHealth=Health(x,y)
        all_health.add(newHealth)
    f=40
    random_cells4=random.sample(maze1.grid_cells,f)
    for i in range(f):
        x=random_cells4[i].x*tile_size+tile_size/4
        y=random_cells4[i].y*tile_size+tile_size/4
        newTrap=Trap(x,y,theme)
        all_traps.add(newTrap)
    e=25
    random_cells5=random.sample(maze1.grid_cells,e)
    for i in range(e):
        x=random_cells5[i].x*tile_size+tile_size/4
        y=random_cells5[i].y*tile_size+tile_size/4
        newEnemy=Enemy(x,y,rows,cols,tile_size,theme)
        all_enemies.add(newEnemy)
    
    # all the counters for implementing game scores and other things.
    coin_counter=0
    gem_counter=0
    health_counter=0
    trap_counter=0
    sprite_health=200 #this is the maximum health of a sprite you cannot have more than that.

    start_time=pygame.time.get_ticks()
    last_speed_update=start_time
    #entering the main game loop.
    running=True
    while running:
        clock.tick(FPS)
        #TODO : CHANGE THE BACKGROUNDS ACCORDING TO RESPECTIVE THEMES
        if theme=='dino':
            BG1=pygame.image.load("resources/forest.png")
            PADDING_BG=pygame.image.load("resources/dino_theme_padding.png")
            SURFACE1.blit(BG1,(0,0))
            ENDPOINT=pygame.image.load('resources/endpoint.png')
            SURFACE1.blit(ENDPOINT,(maze_size-50,maze_size-50))
            SCREEN1.blit(PADDING_BG,(0,0))
            SCREEN1.fill(pygame.Color("#322001"),side_bar_rect)
        
        if theme=='zombie':
            BG1=pygame.image.load("resources/zombie_wallpaper.png")
            PADDING_BG=pygame.image.load("resources/zombie_padding.png")
            SURFACE1.blit(BG1,(0,0))
            ENDPOINT=pygame.image.load('resources/endpoint.png')
            SURFACE1.blit(ENDPOINT,(maze_size-50,maze_size-50))
            SCREEN1.blit(PADDING_BG,(0,0))
            SCREEN1.fill(pygame.Color("#322001"),side_bar_rect)

        pygame.display.set_caption("LEVEL 3")

        total_time=220
        current_time=pygame.time.get_ticks()
        elapsed_time=(current_time-start_time)//1000
        display_time=total_time-elapsed_time
        display_time=str(display_time)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                my_sprite.left_pressed=True
            if event.key==pygame.K_RIGHT:
                my_sprite.right_pressed=True
            if event.key==pygame.K_UP:
                my_sprite.up_pressed=True
            if event.key==pygame.K_DOWN:
                my_sprite.down_pressed=True
            my_sprite.check_move(tile_size,maze1.grid_cells,maze1.thickness)
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                my_sprite.left_pressed=False
            if event.key==pygame.K_RIGHT:
                my_sprite.right_pressed=False
            if event.key==pygame.K_UP:
                my_sprite.up_pressed=False
            if event.key==pygame.K_DOWN:
                my_sprite.down_pressed=False
            my_sprite.check_move(tile_size,maze1.grid_cells,maze1.thickness)

        ##stimulating the enemy randomly

        keys_choice=['leftdown','rightdown','updown','downdown','leftup','rightup','upup','downup']
        
        for random_enemy in all_enemies:

            random_key=random.choice(keys_choice)

            if random_key=='leftdown':
                random_enemy.left_pressed=True

            if random_key=='rightdown':
                random_enemy.right_pressed=True

            if random_key=='updown':
                random_enemy.up_pressed=True

            if random_key=='downdown':
                random_enemy.down_pressed=True

            if random_key=='leftup':
                random_enemy.left_pressed=False

            if random_key=='rightup':
                random_enemy.right_pressed=False

            if random_key=='upup':
                random_enemy.up_pressed=False

            if random_key=='downup':
                random_enemy.down_pressed=False

    #drawing collectibles cells and everything else on the map and updating them.
        [cell.draw(SURFACE1,tile_size) for cell in maze1.grid_cells]
        all_coins.draw(SURFACE1)
        all_coins.update()

        all_gems.draw(SURFACE1)
        all_gems.update()

        all_health.draw(SURFACE1)
        all_health.update()

        all_traps.draw(SURFACE1)
        all_traps.update()
        
        all_sprites.draw(SURFACE1)
        all_sprites.update()

        all_enemies.draw(SURFACE1)
        all_enemies.update()

        collisions_coins=pygame.sprite.spritecollide(my_sprite,all_coins,True)
        for coin in collisions_coins:
            sound.coin_sound()
            coin_counter+=1
            print(coin_counter)


        collisions_gems=pygame.sprite.spritecollide(my_sprite,all_gems,True)
        for gem in collisions_gems:
            sound.gem_sound()
            gem_counter+=1
            my_sprite.speed=20
            last_speed_update=pygame.time.get_ticks()
##Gems speed up the sprite for 5 seconds.
        if pygame.time.get_ticks()-last_speed_update>5000:
            my_sprite.speed=10
            

        collisions_health=pygame.sprite.spritecollide(my_sprite,all_health,True)
        for health in collisions_health:
            sound.health_sound()
            if sprite_health>=200:
                sprite_health=sprite_health
            elif sprite_health<200 and sprite_health>190:
                sprite_health=200
            else:
                sprite_health+=10
                

        collisions_traps=pygame.sprite.spritecollide(my_sprite,all_traps,False)
        for trap in collisions_traps:
            sound.trap_sound(theme)
            sprite_health-=3
            if sprite_health<=0:
                pygame.mixer.music.stop()
                gameover_lost(SCREEN,BG,'health',music_path,3)


        collisions_enemy=pygame.sprite.spritecollide(my_sprite,all_enemies,False)
        for enemies in collisions_enemy:
            sound.enemy_sound(theme)
            sprite_health-=5
            if sprite_health<=0:
                pygame.mixer.music.stop()
                gameover_lost(SCREEN,BG,'health',music_path,3)


    #furthur is camera implementation
    #camera will show us screen 2.
    #screen 2 is player.x-100 to player.x+100 and player.y-100 to player.y+100
    #when player is close to boundaries, we fix the display.
        
        curr_x=my_sprite.x
        curr_y=my_sprite.y
        width=361
        
        if curr_x<=width/2 and curr_y<=width/2:
            game_display_rect=pygame.Rect(0,0,width,width)

        elif curr_x+width/2>=maze_size and curr_y+width/2>=maze_size:
            game_display_rect=pygame.Rect(maze_size-width,maze_size-width,width,width)

        elif curr_x+width/2>=maze_size and curr_y<=width/2:
            game_display_rect=pygame.Rect(maze_size-width,0,width,width)

        elif curr_x<=width/2 and curr_y+width/2>=maze_size:
            game_display_rect=pygame.Rect(0,maze_size-width,width,width)

        elif curr_x<=width/2:
            game_display_rect=pygame.Rect(0,curr_y-width/2,width,width)

        elif curr_y<=width/2:
            game_display_rect=pygame.Rect(curr_x-width/2,0,width,width)

        elif curr_y+width/2>=maze_size:
            game_display_rect=pygame.Rect(curr_x-width/2,maze_size-width,width,width)

        elif curr_x+width/2>=maze_size:
            game_display_rect=pygame.Rect(maze_size-width,curr_y-width/2,width,width)

        else:
            game_display_rect=pygame.Rect(curr_x-width/2,curr_y-width/2,width,width)

        score=int(((curr_x+curr_y)//5)*(elapsed_time/total_time)*(elapsed_time/total_time)+sprite_health*2*(elapsed_time/total_time)*(elapsed_time/total_time)+gem_counter*50+coin_counter*20+(total_time-elapsed_time)*10*(elapsed_time/total_time)*(elapsed_time/total_time))
        score=str(score)
        
        SUBSURFACE1=SURFACE1.subsurface(game_display_rect)
        SCREEN1.blit(SUBSURFACE1,(361/2,361/2))


        if my_sprite.isGameOver():
            #before going to gameover screen we need to see the file which contains the leaderboard and add the score accordingly if needed and then that will get displayed in the gameover screen.
            
            file=open('leaderboards/leaderboard3.txt','r')
            names=[]
            scores=[]
            for line in file:
                entries=line.strip().split(',')

                names.append(entries[0].strip())
                scores.append(entries[1].strip())

            if int(score)>=int(scores[0]):
                scores[2]=scores[1]
                scores[1]=scores[0]
                scores[0]=score

                names[2]=names[1]
                names[1]=names[0]
                names[0]=username

            elif int(score)>=int(scores[1]):
                scores[0]=scores[0]
                scores[2]=scores[1]
                scores[1]=score

                names[0]=names[0]
                names[2]=names[1]
                names[1]=username

            elif int(score)>=int(scores[2]):
                scores[0]=scores[0]
                scores[1]=scores[1]
                scores[2]=score

                names[0]=names[0]
                names[1]=names[1]
                names[2]=username

            else:
                scores=scores
                names=names

            file.close()

            with open("leaderboards/leaderboard3.txt",'w') as file:
                file.write(names[0]+','+scores[0]+'\n')
                file.write(names[1]+','+scores[1]+'\n')
                file.write(names[2]+','+scores[2]+'\n')


            #now that we have our updated our leaderboard according to the current scorecard,
            #we will write that in our leaderboard1.txt file.


                ##add health to sidebar.
                ##add lost of health in gameover_lost

            pygame.mixer.music.stop()
            gameover(SCREEN,BG,score,music_path,3)

        if int(display_time)<0:
            pygame.mixer.music.stop()
            gameover_lost(SCREEN,BG,'time',music_path,3)
        BG_SIDE=pygame.image.load('resources/BG_SIDE.png')
        SCREEN1.blit(BG_SIDE,(722,0))
        sidebar.sidebar_text(SCREEN1,score,display_time,sprite_health)
        pygame.display.flip()

def gameover(SCREEN,BG,score,music_path,level):
    file1=None
    if level==1:
        file1=open('leaderboards/leaderboard1.txt','r')
    elif level==2:
        file1=open('leaderboards/leaderboard2.txt','r')
    elif level==3:
        file1=open('leaderboards/leaderboard3.txt','r')

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
    HIGH_SCORE_1_RECT=HIGH_SCORE_1_TEXT.get_rect(center=(540,350))

    HIGH_SCORE_2_TEXT=font.get_font(30).render("2."+name2+" "+score2, True, "#732c02")
    HIGH_SCORE_2_RECT=HIGH_SCORE_2_TEXT.get_rect(center=(540,425))

    HIGH_SCORE_3_TEXT=font.get_font(30).render("3."+name3+" "+score3, True, "#732c02")
    HIGH_SCORE_3_RECT=HIGH_SCORE_3_TEXT.get_rect(center=(540,500))

    #MAIN_MENU_BUTTON=Button(pygame.image.load("resources/wooden_interface/1.png"),(540,400),"MAIN MENU",font.get_font(65),"#93ff10","#73ff10")
    QUIT_BUTTON=Button(pygame.image.load("resources/wooden_interface/2.png"),(540,625),"QUIT",font.get_font(40),"#93ff10","#73ff10")
    LEADERBOARD_IMG=pygame.image.load('resources/wooden_interface/leaderboard.png')

    sound.game_won()
    running=True
    while running:
        
        SCREEN.blit(BG,(0,0))
        SCREEN.blit(LEADERBOARD_IMG,(290,80))
        SCREEN.blit(HIGH_SCORE_1_TEXT,HIGH_SCORE_1_RECT)
        SCREEN.blit(HIGH_SCORE_2_TEXT,HIGH_SCORE_2_RECT)
        SCREEN.blit(HIGH_SCORE_3_TEXT,HIGH_SCORE_3_RECT)

        GAMEOVER_TEXT = font.get_font(60).render("YOU WON", True, "#732c02")
        GAMEOVER_RECT = GAMEOVER_TEXT.get_rect(center=(540, 55))

        LEADERBOARD_TEXT=font.get_font(35).render("LEADERBOARD", True, "#732c02")
        LEADERBOARD_RECT=LEADERBOARD_TEXT.get_rect(center=(540,260))

        score_display="SCORE:"+score

        YOURSCORE_TEXT=font.get_font(40).render(score_display,True,"#732c02")
        YOURSCORE_RECT=YOURSCORE_TEXT.get_rect(center=(540,180))


        SCREEN.blit(GAMEOVER_TEXT,GAMEOVER_RECT)
        SCREEN.blit(YOURSCORE_TEXT,YOURSCORE_RECT)
        SCREEN.blit(LEADERBOARD_TEXT,LEADERBOARD_RECT)

        MENU_MOUSE_POS=pygame.mouse.get_pos()

        pygame.display.set_caption("GAME OVER")

        QUIT_BUTTON.changeColor(MENU_MOUSE_POS)
        QUIT_BUTTON.update(SCREEN)

        #MAIN_MENU_BUTTON.changeColor(MENU_MOUSE_POS)
        #MAIN_MENU_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                #if MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #sound.button_click_sound()
                    #main_menu(SCREEN,BG,music_path)

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    pygame.quit()
                    sys.exit()
                    
        
        pygame.display.flip()

def gameover_lost(SCREEN,BG,event,music_path,level):
    file1=None
    if level==1:
        file1=open('leaderboards/leaderboard1.txt','r')
    elif level==2:
        file1=open('leaderboards/leaderboard2.txt','r')
    elif level==3:
        file1=open('leaderboards/leaderboard3.txt','r')

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
    HIGH_SCORE_1_RECT=HIGH_SCORE_1_TEXT.get_rect(center=(540,300))

    HIGH_SCORE_2_TEXT=font.get_font(30).render("2."+name2+" "+score2, True, "#732c02")
    HIGH_SCORE_2_RECT=HIGH_SCORE_2_TEXT.get_rect(center=(540,400))

    HIGH_SCORE_3_TEXT=font.get_font(30).render("3."+name3+" "+score3, True, "#732c02")
    HIGH_SCORE_3_RECT=HIGH_SCORE_3_TEXT.get_rect(center=(540,500))

    #MAIN_MENU_BUTTON=Button(pygame.image.load("resources/wooden_interface/1.png"),(540,300),"MAIN MENU",font.get_font(65),"#93ff10","#73ff10")
    QUIT_BUTTON=Button(pygame.image.load("resources/wooden_interface/2.png"),(540,625),"QUIT",font.get_font(40),"#93ff10","#73ff10")
    LEADERBOARD_IMG=pygame.image.load('resources/wooden_interface/leaderboard.png')

    sound.game_lost()
    running=True
    while running:
        
        SCREEN.blit(BG,(0,0))
        SCREEN.blit(LEADERBOARD_IMG,(290,80))
        SCREEN.blit(HIGH_SCORE_1_TEXT,HIGH_SCORE_1_RECT)
        SCREEN.blit(HIGH_SCORE_2_TEXT,HIGH_SCORE_2_RECT)
        SCREEN.blit(HIGH_SCORE_3_TEXT,HIGH_SCORE_3_RECT)

        if (event=='health'):

            GAMEOVER_TEXT = font.get_font(35).render("BE HEALTHIER NEXT TIME", True, "#732c02")
            GAMEOVER_RECT = GAMEOVER_TEXT.get_rect(center=(540, 55))

            LEADERBOARD_TEXT=font.get_font(35).render("LEADERBOARD", True, "#732c02")
            LEADERBOARD_RECT=LEADERBOARD_TEXT.get_rect(center=(540,200))

        if (event=='time'):

            GAMEOVER_TEXT = font.get_font(50).render("BE QUICKER NEXT TIME", True, "#732c02")
            GAMEOVER_RECT = GAMEOVER_TEXT.get_rect(center=(540, 55))

            LEADERBOARD_TEXT=font.get_font(35).render("LEADERBOARD", True, "#732c02")
            LEADERBOARD_RECT=LEADERBOARD_TEXT.get_rect(center=(540,200))




        

        


        SCREEN.blit(GAMEOVER_TEXT,GAMEOVER_RECT)
        SCREEN.blit(LEADERBOARD_TEXT,LEADERBOARD_RECT)
        
        MENU_MOUSE_POS=pygame.mouse.get_pos()

        pygame.display.set_caption("GAME OVER")

        QUIT_BUTTON.changeColor(MENU_MOUSE_POS)
        QUIT_BUTTON.update(SCREEN)

        #MAIN_MENU_BUTTON.changeColor(MENU_MOUSE_POS)
        #MAIN_MENU_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                #if MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #sound.button_click_sound()
                    #main_menu(SCREEN,BG,music_path)

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound.button_click_sound()
                    pygame.quit()
                    sys.exit()
                    
        
        pygame.display.flip()

    
