import pygame

##This is our main character class. 
#Our main characters move according to the keyboard inputs provided to it. 
#Also the animation frames change according to the direction of movement which gives a real character like feel and 
#hence enhances the gaming experience. This also has collision detection implemented with the enemies, traps, coins, gems, health. All of which is implemented in the score. The functions are also present for preventing passing through walls by the player.

class Sprite(pygame.sprite.Sprite):
    def __init__(self,x,y,rows,cols,tile_size,theme):

        super().__init__()
        self.x=int(x)
        self.y=int(y)
        self.rows=rows
        self.cols=cols
        self.tile_size=tile_size
        ##here x and y are the actual positiions not indices.
        self.velX=0
        self.velY=0
        self.player_size=30
        #self.image=pygame.image.load(image_path).convert_alpha()
        #self.rect=self.image.get_rect()
        '''self.rect.x=self.x
        self.rect.y=self.y'''
        self.speed=10
        self.left_pressed=False
        self.right_pressed=False
        self.up_pressed=False
        self.down_pressed=False
        self.health=100
        
        if theme=='dino':
            self.frames_up=[
                pygame.image.load('resources/dino/tile000.png').convert_alpha(),
                pygame.image.load('resources/dino/tile001.png').convert_alpha(),
                pygame.image.load('resources/dino/tile002.png').convert_alpha(),
                pygame.image.load('resources/dino/tile003.png').convert_alpha(),
                pygame.image.load('resources/dino/tile004.png').convert_alpha(),
                pygame.image.load('resources/dino/tile005.png').convert_alpha(),
                pygame.image.load('resources/dino/tile006.png').convert_alpha(),
                pygame.image.load('resources/dino/tile007.png').convert_alpha(),
                pygame.image.load('resources/dino/tile008.png').convert_alpha(),
                pygame.image.load('resources/dino/tile009.png').convert_alpha(),
                pygame.image.load('resources/dino/tile010.png').convert_alpha(),
                pygame.image.load('resources/dino/tile011.png').convert_alpha(),
                pygame.image.load('resources/dino/tile012.png').convert_alpha(),
                pygame.image.load('resources/dino/tile013.png').convert_alpha(),
                pygame.image.load('resources/dino/tile014.png').convert_alpha()
            ]
            self.frames_down=[
                pygame.image.load('resources/dino/tile000.png').convert_alpha(),
                pygame.image.load('resources/dino/tile001.png').convert_alpha(),
                pygame.image.load('resources/dino/tile002.png').convert_alpha(),
                pygame.image.load('resources/dino/tile003.png').convert_alpha(),
                pygame.image.load('resources/dino/tile004.png').convert_alpha(),
                pygame.image.load('resources/dino/tile005.png').convert_alpha(),
                pygame.image.load('resources/dino/tile006.png').convert_alpha(),
                pygame.image.load('resources/dino/tile007.png').convert_alpha(),
                pygame.image.load('resources/dino/tile008.png').convert_alpha(),
                pygame.image.load('resources/dino/tile009.png').convert_alpha(),
                pygame.image.load('resources/dino/tile010.png').convert_alpha(),
                pygame.image.load('resources/dino/tile011.png').convert_alpha(),
                pygame.image.load('resources/dino/tile012.png').convert_alpha(),
                pygame.image.load('resources/dino/tile013.png').convert_alpha(),
                pygame.image.load('resources/dino/tile014.png').convert_alpha()
            ]
            self.frames_left=[
                pygame.image.load('resources/dino/tile000.png').convert_alpha(),
                pygame.image.load('resources/dino/tile001.png').convert_alpha(),
                pygame.image.load('resources/dino/tile002.png').convert_alpha(),
                pygame.image.load('resources/dino/tile003.png').convert_alpha(),
                pygame.image.load('resources/dino/tile004.png').convert_alpha(),
                pygame.image.load('resources/dino/tile005.png').convert_alpha(),
                pygame.image.load('resources/dino/tile006.png').convert_alpha(),
                pygame.image.load('resources/dino/tile007.png').convert_alpha(),
                pygame.image.load('resources/dino/tile008.png').convert_alpha(),
                pygame.image.load('resources/dino/tile009.png').convert_alpha(),
                pygame.image.load('resources/dino/tile010.png').convert_alpha(),
                pygame.image.load('resources/dino/tile011.png').convert_alpha(),
                pygame.image.load('resources/dino/tile012.png').convert_alpha(),
                pygame.image.load('resources/dino/tile013.png').convert_alpha(),
                pygame.image.load('resources/dino/tile014.png').convert_alpha()
            ]
            self.frames_right=[
                pygame.image.load('resources/dino/tile000.png').convert_alpha(),
                pygame.image.load('resources/dino/tile001.png').convert_alpha(),
                pygame.image.load('resources/dino/tile002.png').convert_alpha(),
                pygame.image.load('resources/dino/tile003.png').convert_alpha(),
                pygame.image.load('resources/dino/tile004.png').convert_alpha(),
                pygame.image.load('resources/dino/tile005.png').convert_alpha(),
                pygame.image.load('resources/dino/tile006.png').convert_alpha(),
                pygame.image.load('resources/dino/tile007.png').convert_alpha(),
                pygame.image.load('resources/dino/tile008.png').convert_alpha(),
                pygame.image.load('resources/dino/tile009.png').convert_alpha(),
                pygame.image.load('resources/dino/tile010.png').convert_alpha(),
                pygame.image.load('resources/dino/tile011.png').convert_alpha(),
                pygame.image.load('resources/dino/tile012.png').convert_alpha(),
                pygame.image.load('resources/dino/tile013.png').convert_alpha(),
                pygame.image.load('resources/dino/tile014.png').convert_alpha()
            ]

        if theme=='zombie':
            self.frames_up=[
                pygame.image.load('resources/sprite2/tile012.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile013.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile014.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile015.png').convert_alpha()
            ]
            self.frames_down=[
                pygame.image.load('resources/sprite2/tile000.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile001.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile002.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile003.png').convert_alpha()
            ]
            self.frames_left=[
                pygame.image.load('resources/sprite2/tile004.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile005.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile006.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile007.png').convert_alpha()

            ]
            self.frames_right=[
                pygame.image.load('resources/sprite2/tile008.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile009.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile010.png').convert_alpha(),
                pygame.image.load('resources/sprite2/tile011.png').convert_alpha(),

            ]

        self.frame_number=0
        self.image=self.frames_right[self.frame_number]
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        
        self.animation_speed=0.1
    #def draw(self,SCREEN):
        #pygame.draw.rect(SCREEN,self.color,self.rect)
        self.last_update=pygame.time.get_ticks()

    def current_cell(self,x,y,grid_cells):
        for cell in grid_cells:
            if cell.x==x and cell.y==y:
                return cell
            
    def check_move(self,tile_size,grid_cells,thickness):
        current_x_indice=self.x // tile_size
        current_y_indice=self.y // tile_size

        current_cell1=self.current_cell(current_x_indice,current_y_indice,grid_cells)
        current_cell_abs_x=tile_size*current_x_indice
        current_cell_abs_y=tile_size*current_y_indice


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
                    self.down_pressed=False

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

    def isGameOver(self):
        if self.x+self.player_size>=self.tile_size*self.cols and self.y+self.player_size>=self.tile_size*self.rows:
            return True
        else:
            return False
        



        