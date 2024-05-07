import pygame
##This file has all the sounds loaded so that the sounds can be called by other screens 
##just by calling the functions from this file and hence easing accessibility.
def button_click_sound():
    click_sound=pygame.mixer.Sound('resources/sounds/button_click.mp3')
    click_sound.play()

def coin_sound():
    coin_collect=pygame.mixer.Sound('resources/sounds/coin.mp3')
    coin_collect.play()

def gem_sound():
    gem_collect=pygame.mixer.Sound('resources/sounds/gemcollect.mp3')
    gem_collect.play()

def health_sound():
    health_collect=pygame.mixer.Sound('resources/sounds/health.mp3')
    health_collect.play()

def trap_sound(theme):
    if theme=='dino':
        fire_encounter=pygame.mixer.Sound('resources/sounds/fire.mp3')
        fire_encounter.play()

    #TODO: write for another theme
    if theme=='zombie':
        zombie_trap=pygame.mixer.Sound('resources/sounds/zombie_trap.mp3')
        zombie_trap.play()

def enemy_sound(theme):
    if theme=='dino':
        dragon_encounter=pygame.mixer.Sound('resources/sounds/dragon_roar.mp3')
        dragon_encounter.play()

    #TODO: write for another theme
    if theme=='zombie':
        zombie_encounter=pygame.mixer.Sound('resources/sounds/zombie_sound.mp3')
        zombie_encounter.play()

def typing_sound():
    typing_click=pygame.mixer.Sound('resources/sounds/typing_sound.mp3')
    typing_click.play()

def game_lost():
    game_lost_sound=pygame.mixer.Sound('resources/sounds/game_lost.mp3')
    game_lost_sound.play()

def game_won():
    game_won_sound=pygame.mixer.Sound('resources/sounds/game_won.mp3')
    game_won_sound.play()

def sound_on():
    on_sound=pygame.mixer.Sound('resources/sounds/sound_on.mp3')
    on_sound.play()

def sound_off():
    off_sound=pygame.mixer.Sound('resources/sounds/sound_off.mp3')
    off_sound.play()

    

