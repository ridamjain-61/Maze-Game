import pygame

class Enemy(pygame.sprite.Sprite):

    ##This file contains the implementation of the enemy class. There are two types of enemies according to theme. If the theme is Jurassic then the enemies are flying dragons, if the theme is Zombie, then the enemies are the zombies.
    #The implementation of these again involves sprites in pygame. These are animated according to their direction of movement. In other words, these have different image frames for each direction of movement.
    def __init__(self,x,y,rows,cols,tile_size,theme):
        super().__init__()
        self.x=x
        self.y=y

        self.rows=rows
        self.cols=cols

        self.tile_size=tile_size

        self.player_size=30

        self.speed=10
        ##each direction has separate animations according to instantaneous direction of movement.
        self.left_pressed=False
        self.right_pressed=False
        self.up_pressed=False
        self.down_pressed=False
        if theme=='dino':
            self.frames_up=[
                pygame.image.load('resources/dragon/tile000.png').convert_alpha(),
                pygame.image.load('resources/dragon/tile001.png').convert_alpha(),
                pygame.image.load('resources/dragon/tile002.png').convert_alpha()
            ]
            self.frames_down=[
                pygame.image.load('resources/dragon/tile006.png').convert_alpha(),
                pygame.image.load('resources/dragon/tile007.png').convert_alpha(),
                pygame.image.load('resources/dragon/tile008.png').convert_alpha()
            ]
            self.frames_right=[
                pygame.image.load('resources/dragon/tile003.png').convert_alpha(),
                pygame.image.load('resources/dragon/tile004.png').convert_alpha(),
                pygame.image.load('resources/dragon/tile005.png').convert_alpha()
            ]
            self.frames_left=[
                pygame.image.load('resources/dragon/tile009.png').convert_alpha(),
                pygame.image.load('resources/dragon/tile010.png').convert_alpha(),
                pygame.image.load('resources/dragon/tile011.png').convert_alpha()
            ]
        if theme=='zombie':
            self.frames_up=[ 
                pygame.image.load('resources/zombie_new/tile000.png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile001.png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile002.png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile003.png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile004.png').convert_alpha()
            ]
            self.frames_down=[ 
                pygame.image.load('resources/zombie_new/tile000 (2).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile001 (2).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile002 (2).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile003 (2).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile004 (2).png').convert_alpha()
                
                
            ]
            self.frames_left=[ 
                pygame.image.load('resources/zombie_new/tile000 (2).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile001 (2).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile002 (2).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile003 (2).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile004 (2).png').convert_alpha()
            ]
            self.frames_right=[ 
                pygame.image.load('resources/zombie_new/tile000 (3).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile001 (3).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile002 (3).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile003 (3).png').convert_alpha(),
                pygame.image.load('resources/zombie_new/tile004 (3).png').convert_alpha()
            ]
            
        self.frame_number=0
        self.image=self.frames_right[self.frame_number]
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

        self.animation_speed=0.1

        self.last_update=pygame.time.get_ticks()
        #just initialising it right now 
        # this will get updated whenever the next frame is used in animation


    def current_cell(self,x,y,grid_cells):
        for cell in grid_cells:
            if cell.x==x and cell.y==y:
                return cell
            


    

    def update(self):

        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            
            self.velX = -self.speed
            now=pygame.time.get_ticks()
            if now-self.last_update>self.animation_speed*1000:
                self.frame_number=(self.frame_number+1)%len(self.frames_left)
                self.image=self.frames_left[self.frame_number]
                self.last_update=now

        if self.right_pressed and not self.left_pressed:
            
            self.velX = self.speed
            now=pygame.time.get_ticks()
            if now-self.last_update>self.animation_speed*1000:
                self.frame_number=(self.frame_number+1)%len(self.frames_right)
                self.image=self.frames_right[self.frame_number]
                self.last_update=now

        if self.up_pressed and not self.down_pressed:
            
            self.velY = -self.speed
            now=pygame.time.get_ticks()
            if now-self.last_update>self.animation_speed*1000:
                self.frame_number=(self.frame_number+1)%len(self.frames_up)
                self.image=self.frames_up[self.frame_number]
                self.last_update=now

        if self.down_pressed and not self.up_pressed:
            
            self.velY = self.speed
            now=pygame.time.get_ticks()
            if now-self.last_update>self.animation_speed*1000:
                self.frame_number=(self.frame_number+1)%len(self.frames_down)
                self.image=self.frames_down[self.frame_number]
                self.last_update=now

        self.x += self.velX
        self.y += self.velY
                
        #self.rect=pygame.Rect(int(self.x),int(self.y),self.player_size,self.player_size)
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y



        ''' def check_move(self,tile_size,grid_cells,thickness):
        current_x_indice=self.x//tile_size

        current_y_indice=self.y//tile_size

        current_cell1=self.current_cell(current_x_indice,current_y_indice,grid_cells)
        current_cell_abs_x=current_x_indice*tile_size
        current_cell_abs_y=current_y_indice*tile_size

        if self.left_pressed:
            if current_cell1.walls['left']:
                if self.x<=current_cell_abs_x+thickness:
                    self.left_pressed=False

            if self.right_pressed:
                if current_cell1.walls['right']:
                    if self.x>=current_cell_abs_x+tile_size-thickness-self.player_size:
                        self.right_pressed=False


            if self.up_pressed:
                if current_cell1.walls['up']:
                    if self.y<=current_cell_abs_y+thickness:
                        self.up_pressed=False

            if self.down_pressed:
                if current_cell1.walls['down']:
                    if self.y>=current_cell_abs_y+tile_size-thickness-self.player_size:
                        self.down_pressed=False'''