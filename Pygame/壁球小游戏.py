# 壁球小游戏（综合型）
import pygame
import sys  # 库的引用

pygame.init()
# icon = pygame.image.load("D:/Personal/picture/手机/小姐姐/寂寥的心.jpg")
# pygame.display.set_icon(icon)
size = width, height = 600, 400
speed = [1, 1]  # [v1, v2] v1代表向右的运动速度，v2代表向上的运动速度，负值表示反方向运动
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Pygame壁球小游戏")
ball = pygame.image.load("D:/Study/Python/词云图片/花哨五角星.jpg")
ballrect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()  # 初始化
pygame.mixer.music.load("D:/Personal/music/Local/Akie秋绘 - なんでもないや.mp3")
pygame.mixer.music.play(1)

while True:
    for event in pygame.event.get():    # pygame实时获取事件变化
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else(abs(speed[0])-1)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0]-1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else(abs(speed[1])-1)*int(speed[1]/abs(speed[1]))
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    if pygame.display.get_active():     # 判断窗口是否屏幕绘制(最大化)，是则返回True，否则返回False
        ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]

    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.display.update()     # 重新绘制整个窗口
    fclock.tick(fps)    # 窗口刷新
