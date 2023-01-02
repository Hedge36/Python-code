# draw learning
import pygame
import sys
import pygame.freetype

pygame.init()
# screen = pygame.display.set_mode((1600, 1000))
screen = pygame.display.set_mode((1600, 1000), pygame.FULLSCREEN)
pygame.display.set_caption("劝人学习，天打雷劈")
GOLD = 255, 251, 0

f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
f1rect = f1.render_to(screen, (400, 300), "学习", fgcolor=GOLD, size=390)
f2surf, f2rect = f1.render("劝人学习，天打雷劈", fgcolor=GOLD, size=15)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.blit(f2surf, (200, 200))
    pygame.display.update()
