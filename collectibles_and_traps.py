import pygame
##This file contains the basic class Cell. This class contains the properties of each cell of the grid of the maze. 
##The basic declaration of the Cell contains its x and y indices, and the thickness of wall around it. This also contains some functions for the generation of the maze which is done in maze.py file.
class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):

        super().__init__()
        
        self.x=x
        self.y=y
        

        ##these frames are different images of the sprite in different orientations which gives the appearance of animation to the sprite.

        self.frames=[
            pygame.image.load('resources/coin_new/tile000.png').convert_alpha(),
            pygame.image.load('resources/coin_new/tile001.png').convert_alpha(),
            pygame.image.load('resources/coin_new/tile002.png').convert_alpha(),
            pygame.image.load('resources/coin_new/tile003.png').convert_alpha(),
            pygame.image.load('resources/coin_new/tile004.png').convert_alpha(),
            pygame.image.load('resources/coin_new/tile005.png').convert_alpha(),
            pygame.image.load('resources/coin_new/tile006.png').convert_alpha(),
            pygame.image.load('resources/coin_new/tile007.png').convert_alpha()
        ]

        self.frame_number=0
        self.image=self.frames[self.frame_number]
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        
        self.animation_speed=0.1
        #that is we are refreshing it once in 0.2 seconds
        self.last_update=pygame.time.get_ticks()

    def update(self):
        ##updating the sprite according to time passed, we chose the animation speed to be 0.1 so in every 0.1 seconds, the sprite is updated.
        now=pygame.time.get_ticks()
        if now-self.last_update>self.animation_speed*1000:
            self.frame_number=(self.frame_number+1)%len(self.frames)
            self.image=self.frames[self.frame_number]
            self.last_update=now


class Gem(pygame.sprite.Sprite):
    def __init__(self,x,y):

        super().__init__()

        self.x=x
        self.y=y


        self.frames=[
            pygame.image.load('resources/gems/tile000.png').convert_alpha(),
            pygame.image.load('resources/gems/tile001.png').convert_alpha(),
            pygame.image.load('resources/gems/tile002.png').convert_alpha(),
            pygame.image.load('resources/gems/tile003.png').convert_alpha(),
            pygame.image.load('resources/gems/tile004.png').convert_alpha(),
            pygame.image.load('resources/gems/tile005.png').convert_alpha(),
            pygame.image.load('resources/gems/tile006.png').convert_alpha(),
            pygame.image.load('resources/gems/tile007.png').convert_alpha()
        ]

        self.frame_number=0

        self.image=self.frames[self.frame_number]
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.animation_speed=0.1

        self.last_update=pygame.time.get_ticks()

    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>self.animation_speed*1000:
            self.frame_number=(self.frame_number+1)%len(self.frames)
            self.image=self.frames[self.frame_number]
            self.last_update=now


class Health(pygame.sprite.Sprite):
    def __init__(self,x,y):

        super().__init__()

        self.x=x
        self.y=y


        self.frames=[
            pygame.image.load('resources/health/tile000.png').convert_alpha(),
            pygame.image.load('resources/health/tile001.png').convert_alpha(),
            pygame.image.load('resources/health/tile002.png').convert_alpha(),
            pygame.image.load('resources/health/tile003.png').convert_alpha(),
            pygame.image.load('resources/health/tile004.png').convert_alpha(),
            pygame.image.load('resources/health/tile005.png').convert_alpha(),
            pygame.image.load('resources/health/tile006.png').convert_alpha()
        ]

        self.frame_number=0

        self.image=self.frames[self.frame_number]
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.animation_speed=0.1

        self.last_update=pygame.time.get_ticks()

    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>self.animation_speed*1000:
            self.frame_number=(self.frame_number+1)%len(self.frames)
            self.image=self.frames[self.frame_number]
            self.last_update=now


class Trap(pygame.sprite.Sprite):
    def __init__(self,x,y,theme):

        super().__init__()

        self.x=x
        self.y=y

        if theme=='dino':
            self.frames=[
                pygame.image.load('resources/bluefire/tile000.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile001.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile002.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile003.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile004.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile005.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile006.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile007.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile008.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile009.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile010.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile011.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile012.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile013.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile014.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile015.png').convert_alpha(),
                pygame.image.load('resources/bluefire/tile016.png').convert_alpha()
                
            ]
        if theme=='zombie':
            self.frames=[ 
                pygame.image.load('resources/pumpkin/tile000.png').convert_alpha(),
                pygame.image.load('resources/pumpkin/tile001.png').convert_alpha(),
                pygame.image.load('resources/pumpkin/tile002.png').convert_alpha(),
                pygame.image.load('resources/pumpkin/tile003.png').convert_alpha(),
                pygame.image.load('resources/pumpkin/tile004.png').convert_alpha(),
                pygame.image.load('resources/pumpkin/tile005.png').convert_alpha()
            ]

        self.frame_number=0
        self.image=self.frames[self.frame_number]
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.animation_speed=0.1

        self.last_update=pygame.time.get_ticks()

    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>self.animation_speed*1000:
            self.frame_number=(self.frame_number+1)%len(self.frames)
            self.image=self.frames[self.frame_number]
            self.last_update=now
    