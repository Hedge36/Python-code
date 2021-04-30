# 键盘事件响应
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame事件处理")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN]:", "#", event.key, event.mod)
            else:
                print("[KEYDOWN]:", event.unicode, event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            print("[MOUSEMOTION]:", event.pos, event.rel, event.buttons)
#                       返回鼠标的属性： 当前坐标   相对运动距离     鼠标状态
        elif event.type == pygame.MOUSEBUTTONUP:
            print("[MOUSEBUTTONUP]:", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MOUSEBUTTONDOWN]:", event.pos, event.button)
        pygame.display.update()
