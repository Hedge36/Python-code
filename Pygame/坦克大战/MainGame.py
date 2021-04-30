from Object import *
import os


class MainGame:
    # 类属性：窗口
    WINDOW = None
    SCREEN_WIDTH = 1200  # 20
    SCREEN_HEIGHT = 660  # 11
    COLOR_BG = pygame.Color('black')
    ICON = pygame.image.load('img/ICON.gif')
    DELAY = 2
    # Object
    TANK_Player = None
    TANK_ROBOTS = []
    BULLETS = []
    OBSTACLES = []
    EXPLODE = []
    COUNT_ROBOTS = 2
    MAP = [
        Rect(0, 180),
        Rect(60, 180),
        Rect(120, 180),
        Rect(180, 180)
    ]
    RECT_INIT = [
        Rect(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)),
        Rect(int(60), int(60)),
        Rect(int(120), int(120))
    ]

    def __init__(self):
        self.robot_count = MainGame.COUNT_ROBOTS

    @staticmethod
    def end_game():
        print('END')
        exit()

    @staticmethod
    def end_game_judge():
        if not MainGame.TANK_Player.is_live:
            MainGame.end_game()

    @staticmethod
    def creating(class_name):
        tmp = []
        if class_name == 'Obstacle':
            for i in range(len(MainGame.MAP)):
                obstacle = Obstacle(MainGame.MAP[i])
                tmp.append(obstacle)
            return tmp
        elif class_name == 'TankRobot':
            for i in range(MainGame.COUNT_ROBOTS):
                i += 1
                tank_robot = TankRobot(MainGame.RECT_INIT[i], MainGame.TANK_Player)
                tmp.append(tank_robot)
            return tmp

    def display(self, obj):
        if isinstance(obj, TankPlayer):
            MainGame.TANK_Player.display_is(MainGame.WINDOW)
        if isinstance(obj, list):
            for i in obj:
                if not i.display_is(MainGame.WINDOW):
                    if isinstance(i, TankRobot):
                        MainGame.EXPLODE.append(Explode(i.rect))
                        self.robot_count -= 1
                    elif isinstance(i, Bullet):
                            i.owner.bullet_count -= 1
                    obj.remove(i)
                    del i

    @staticmethod
    def move(obj):
        if isinstance(obj, list):
            for i in obj:
                if i.is_move:
                    if not i.impact_checking(MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT, [MainGame.TANK_Player] + MainGame.OBSTACLES + MainGame.TANK_ROBOTS):
                        i.move()
                    elif isinstance(i, TankRobot):
                        i.auto_direction()
        else:
            if obj.is_move:
                if not obj.impact_checking(MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT, MainGame.OBSTACLES + MainGame.TANK_ROBOTS):
                    obj.move()
                    # print('({}, {})'.format(obj.rect.left, obj.rect.top))

    @staticmethod
    def robot_shout(robot_list):
        for i in robot_list:
            temp = i.auto_shout()
            if temp:
                MainGame.BULLETS.append(temp)

    @staticmethod
    def play_start_music():
        Music('img/start.wav').play()
        pygame.time.delay(4000)

    # 事件处理：1.窗口关闭 2.控制我方坦克
    def get_event(self, tank_player):
        # 获得事件列表
        event_list = pygame.event.get()
        # 处理事件
        for event in event_list:
            # 事件1：窗口关闭
            if event.type == pygame.QUIT:
                self.end_game()
            # 事件2：方向控制 和 移动控制
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    temp = tank_player.shout_player(self.robot_count)
                    if temp:
                        Music('img/hit.wav').play()
                        MainGame.BULLETS.append(temp)
                elif event.key == pygame.K_UP:
                    tank_player.is_move = True
                    tank_player.direction = 0
                    tank_player.state = 0
                elif event.key == pygame.K_DOWN:
                    tank_player.is_move = True
                    tank_player.direction = 1
                    tank_player.state = 1
                elif event.key == pygame.K_LEFT:
                    tank_player.is_move = True
                    tank_player.direction = 2
                    tank_player.state = 2
                elif event.key == pygame.K_RIGHT:
                    tank_player.is_move = True
                    tank_player.direction = 3
                    tank_player.state = 3
            elif event.type == pygame.KEYUP:
                tank_player.is_move = False

    def start_game(self):
        # 窗口初始化
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30)
        pygame.display.init()  # Initialization
        pygame.display.set_caption("Tanks\' War")  # Set caption
        pygame.display.set_icon(MainGame.ICON)  # Set Icon
        MainGame.WINDOW = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 实例创建，并初次展示
        MainGame.WINDOW.fill(MainGame.COLOR_BG)
        MainGame.TANK_Player = TankPlayer(MainGame.RECT_INIT[0])
        self.display(MainGame.TANK_Player)
        MainGame.OBSTACLES = MainGame.creating(class_name='Obstacle')
        self.display(MainGame.OBSTACLES)
        MainGame.TANK_ROBOTS = MainGame.creating(class_name='TankRobot')
        self.display(MainGame.TANK_ROBOTS)
        pygame.display.update()
        # 播放开始音乐
        MainGame.play_start_music()
        # 主循环
        while True:
            # 背景展示
            MainGame.WINDOW.fill(MainGame.COLOR_BG)
            # 实例展示
            self.display(MainGame.TANK_Player)
            self.display(MainGame.TANK_ROBOTS)
            self.display(MainGame.OBSTACLES)
            self.display(MainGame.BULLETS)
            self.display(MainGame.EXPLODE)
            # Get Events
            self.get_event(MainGame.TANK_Player)
            self.robot_shout(MainGame.TANK_ROBOTS)
            # Move
            self.move(MainGame.TANK_Player)
            self.move(MainGame.TANK_ROBOTS)
            self.move(MainGame.BULLETS)
            # 游戏结束检测
            self.end_game_judge()
            # Update
            pygame.display.update()
            pygame.time.delay(MainGame.DELAY)


if __name__ == '__main__':
    MainGame().start_game()