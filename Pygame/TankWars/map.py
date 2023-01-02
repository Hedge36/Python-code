from Object import *
import os


class MainGame:
    # 类属性：窗口
    WINDOW = None
    SCREEN_WIDTH = 1200  # 20
    SCREEN_HEIGHT = 660  # 11
    COLOR_BG = pygame.Color('black')
    ICON = pygame.image.load('img/ICON.gif')
    # Object
    ELEM = None
    MAP = []

    # 事件处理：1.窗口关闭 2.
    def get_event(self, obj):
        # 获得事件列表
        event_list = pygame.event.get()
        # 处理事件
        for event in event_list:
            # 事件1：窗口关闭
            if event.type == pygame.QUIT:
                exit()
            # 事件2：方向控制 和 移动控制
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                elif event.key == pygame.K_UP:
                    obj.move(0)
                elif event.key == pygame.K_DOWN:
                    obj.move(1)
                elif event.key == pygame.K_LEFT:
                    obj.move(2)
                elif event.key == pygame.K_RIGHT:
                    obj.move(3)

    def start_design(self):
        # 窗口初始化
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30)
        pygame.display.init()  # Initialization
        pygame.display.set_caption("Tanks\' War Map Design")  # Set caption
        pygame.display.set_icon(MainGame.ICON)  # Set Icon
        MainGame.WINDOW = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 实例创建
        MainGame.WINDOW.fill(MainGame.COLOR_BG)
        MainGame.ELEM = MapElem(Rect(0, 0))
        # 主循环
        while True:
            # 背景展示
            MainGame.WINDOW.fill(MainGame.COLOR_BG)
            # 实例展示
            MainGame.ELEM.display(MainGame.WINDOW)
            # Get Events
            self.get_event(MainGame.ELEM)
            # Update
            pygame.display.update()


if __name__ == '__main__':
    MainGame().start_design()