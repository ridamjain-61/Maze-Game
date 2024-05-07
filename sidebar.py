import font
import pygame
#5d3614ile contains the blitting instruction of the sidebar which stores the game scores, instructions, health and time left on the side of the game screen.
#5d3614mer also turns red when the time left is less than 10 seconds.

def sidebar_text(SCREEN,score,time,sprite_health):
    USE = font.get_font(30).render("USE", True, "#5d3614")
    USE_RECT = USE.get_rect(center=(722+358/2,50))

    ARROW_KEYS=font.get_font(30).render("ARROW KEYS", True, "#5d3614")
    ARROW_KEYS_RECT=ARROW_KEYS.get_rect(center=(722+358/2,100))
    

    TO_MOVE=font.get_font(30).render("TO MOVE", True, "#5d3614")
    TO_MOVE_RECT=TO_MOVE.get_rect(center=(722+358/2,150))

    if int(time)<=10:
        if int(time)%2!=0:
            TIME=font.get_font(30).render("TIME LEFT", True, "#5d3614")
            TIME_RECT=TIME.get_rect(center=(722+358/2,300))
            
        
            TIME_VALUE=font.get_font(30).render(time, True, "#5d3614")
            TIME_VALUE_RECT=TIME_VALUE.get_rect(center=(722+358/2,350))
        else:
            TIME=font.get_font(30).render("TIME LEFT", True, "red")
            TIME_RECT=TIME.get_rect(center=(722+358/2,300))
            
        
            TIME_VALUE=font.get_font(30).render(time, True, "red")
            TIME_VALUE_RECT=TIME_VALUE.get_rect(center=(722+358/2,350))
            

    else:
        TIME=font.get_font(30).render("TIME LEFT", True, "#5d3614")
        TIME_RECT=TIME.get_rect(center=(722+358/2,300))
        
    
        TIME_VALUE=font.get_font(30).render(time, True, "#5d3614")
        TIME_VALUE_RECT=TIME_VALUE.get_rect(center=(722+358/2,350))


    SCORE=font.get_font(30).render("SCORE", True, "#5d3614")
    SCORE_RECT=SCORE.get_rect(center=(722+358/2,575))

    SCORE_VALUE=font.get_font(30).render(score, True, "#5d3614")
    SCORE_VALUE_RECT=SCORE_VALUE.get_rect(center=(722+358/2,650))

    HEALTH=font.get_font(30).render("HEALTH", True, "#5d3614")
    HEALTH_RECT=HEALTH.get_rect(center=(722+358/2,425))

    if int(sprite_health)>=100:


        HEALTH_VALUE=font.get_font(30).render(str(sprite_health), True, "#1c8510")
        HEALTH_VALUE_RECT=HEALTH_VALUE.get_rect(center=(722+358/2,500))

    else:
        HEALTH_VALUE=font.get_font(30).render(str(sprite_health), True, "red")
        HEALTH_VALUE_RECT=HEALTH_VALUE.get_rect(center=(722+358/2,500))

    SCREEN.blit(USE,USE_RECT)
    SCREEN.blit(ARROW_KEYS,ARROW_KEYS_RECT)
    SCREEN.blit(TO_MOVE,TO_MOVE_RECT)
    SCREEN.blit(TIME,TIME_RECT)
    SCREEN.blit(TIME_VALUE,TIME_VALUE_RECT)
    SCREEN.blit(SCORE,SCORE_RECT)
    SCREEN.blit(SCORE_VALUE,SCORE_VALUE_RECT)
    SCREEN.blit(HEALTH,HEALTH_RECT)
    SCREEN.blit(HEALTH_VALUE,HEALTH_VALUE_RECT)


