import pygame
import copy
import random
from Tools import *


class Object:
    STATE_INIT = 0

    def __init__(self, images, rect):
        self.images = images
        self.state = Object.STATE_INIT
        self.image = self.images[self.state]
        self.rect = self.image.get_rect()
        self.rect.left = rect.left
        self.rect.top = rect.top
        self.is_destroy = False
        self.is_live = True

    def display_is(self, window):
        if self.is_live:
            self.image = self.images[self.state]
            window.blit(self.image, self.rect)
            return True
        else:
            return False


class Motion(Object):
    SPEED_INIT = 1

    def __init__(self, images, rect):
        super().__init__(images, rect)
        self.direction = super().STATE_INIT
        self.rect_last = None
        self.is_collision = False
        self.is_move = False

    def move(self):
        self.rect_last = copy.copy(self.rect)
        if self.direction == 0:
            self.rect.top -= Motion.SPEED_INIT
        elif self.direction == 1:
            self.rect.top += Motion.SPEED_INIT
        elif self.direction == 2:
            self.rect.left -= Motion.SPEED_INIT
        elif self.direction == 3:
            self.rect.left += Motion.SPEED_INIT

    def impact_checking(self, screen_width, screen_height, obj_list=None):
        # 边界碰撞检测
        if self.direction == 0 and self.rect.top < 0:
            self.rect = copy.copy(self.rect_last)
            self.is_collision = True
            return True
        elif self.direction == 1 and self.rect.top + self.rect.height > screen_height:
            self.rect = copy.copy(self.rect_last)
            self.is_collision = True
            return True
        elif self.direction == 2 and self.rect.left < 0:
            self.rect = copy.copy(self.rect_last)
            self.is_collision = True
            return True
        elif self.direction == 3 and self.rect.left + self.rect.width > screen_width:
            self.rect = copy.copy(self.rect_last)
            self.is_collision = True
            return True
        # 物体碰撞检测
        for obj in obj_list:
            if self != obj:
                if is_collision_rect(self.rect, obj.rect):
                    self.rect = self.rect_last
                    self.is_collision = True
                    return True
        # 无碰撞
        self.is_collision = False
        return False


class Tank(Motion):
    TANK_WIDTH = 60
    TANK_HEIGHT = 60

    def __init__(self, images, rect):
        super().__init__(images, rect)
        self.sign = 1
        self.bullet_count = 0
        self.is_destroy = True

    def shout(self):
        left = 0
        top = 0
        rect = Bullet.images[0].get_rect()
        if self.direction == 0:
            left = self.rect.left + int(self.rect.width / 2) - int(rect.width / 2)  # ?
            top = self.rect.top - int(rect.height / 2)
        elif self.direction == 1:
            left = self.rect.left + int(self.rect.width / 2) - int(rect.width / 2)
            top = self.rect.top + self.rect.height
        elif self.direction == 2:
            left = self.rect.left - int(rect.width / 2)
            top = self.rect.top + int(self.rect.width / 2) - int(rect.width / 2)
        elif self.direction == 3:
            left = self.rect.left + self.rect.width
            top = self.rect.top + int(self.rect.width / 2) - int(rect.width / 2)
        return Bullet(Rect(left, top), self.direction, self)

    def move(self):
        self.rect_last = copy.copy(self.rect)
        if self.sign == 0:
            if self.direction == 0:
                self.rect.top -= Motion.SPEED_INIT
            elif self.direction == 1:
                self.rect.top += Motion.SPEED_INIT
            elif self.direction == 2:
                self.rect.left -= Motion.SPEED_INIT
            elif self.direction == 3:
                self.rect.left += Motion.SPEED_INIT
            self.sign = 1
        else:
            self.sign -= 1


class TankPlayer(Tank):
    images = {
        0: pygame.image.load('img/p1tankU.gif'),
        1: pygame.image.load('img/p1tankD.gif'),
        2: pygame.image.load('img/p1tankL.gif'),
        3: pygame.image.load('img/p1tankR.gif')
    }

    def __init__(self, rect):
        super().__init__(TankPlayer.images, rect)

    def shout_player(self, enemy_count):
        if self.bullet_count < enemy_count:
            self.bullet_count += 1
            return self.shout()
        else:
            return False


class TankRobot(Tank):
    images = {
        0: pygame.image.load('img/enemy1U.gif'),
        1: pygame.image.load('img/enemy1D.gif'),
        2: pygame.image.load('img/enemy1L.gif'),
        3: pygame.image.load('img/enemy1R.gif')
    }
    random_direction = {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }
    BULLET_MAX = 1

    def __init__(self, rect, enemy):
        super().__init__(TankRobot.images, rect)
        self.have_bullet = False
        self.enemy = enemy
        self.state = TankRobot.STATE_INIT + 1
        self.direction = TankRobot.STATE_INIT + 1
        self.is_move = True

    def auto_direction(self):
        self.state = random.choice(TankRobot.random_direction[self.direction])
        self.direction = self.state

    def shout_checking(self):
        if self.bullet_count <= TankRobot.BULLET_MAX:
            if self.is_relative_direction():
                if self.direction == 0 or self.direction == 1:
                    rect = Rect(self.rect.left, self.enemy.rect.top)
                else:
                    rect = Rect(self.enemy.rect.left, self.rect.top)
                bullet = Bullet(rect, self.direction, self)
                if is_collision_rect(bullet.rect, self.enemy.rect):
                    del bullet
                    return True
                else:
                    del bullet
                    return False
            else:
                return False

    def auto_shout(self):
        if self.shout_checking():
            self.bullet_count += 1
            return self.shout()
        else:
            return False

    def is_relative_direction(self):
        left = self.enemy.rect.left - self.rect.left
        top = self.enemy.rect.left - self.rect.left
        if left > 0 and top > 0:
            if self.direction == 1 or self.direction == 3:
                return True
        elif left > 0 > top:
            if self.direction == 1 or self.direction == 2:
                return True
        elif left < 0 < top:
            if self.direction == 0 or self.direction == 3:
                return True
        elif left < 0 and top < 0:
            if self.direction == 0 or self.direction == 2:
                return True
        else:
            return False


class Bullet(Motion):
    images = {
        0: pygame.image.load('img/bullet.gif')
    }

    def __init__(self, rect, direction, owner):
        super().__init__(Bullet.images, rect)
        self.direction = direction
        self.owner = owner
        self.is_move = True

    def impact_checking(self, screen_width, screen_height, obj_list=None):
        # 边界碰撞检测
        if self.direction == 0 and self.rect.top < 0:
            self.is_live = False
            self.is_collision = True
            return True
        elif self.direction == 1 and self.rect.top + self.rect.height > screen_height:
            self.is_live = False
            self.is_collision = True
            return True
        elif self.direction == 2 and self.rect.left < 0:
            self.is_live = False
            self.is_collision = True
            return True
        elif self.direction == 3 and self.rect.left + self.rect.width > screen_width:
            self.is_live = False
            self.is_collision = True
            return True
        # 物体碰撞检测
        for obj in obj_list:
            if is_collision_rect(self.rect, obj.rect) and self.owner != obj:
                self.is_live = False
                self.is_collision = True
                # 修改对象的生存状态 ?????
                if obj.is_destroy:
                    obj.is_live = False
                return True
        # 无碰撞
        self.is_collision = False
        return False


class Obstacle(Object):
    images = {
        0: pygame.image.load('img/steels.gif')
    }

    def __init__(self, rect):
        super().__init__(Obstacle.images, rect)


class Explode(Object):
    images = [
        pygame.image.load('img/blast0.gif'),
        pygame.image.load('img/blast1.gif'),
        pygame.image.load('img/blast2.gif'),
        pygame.image.load('img/blast3.gif'),
        pygame.image.load('img/blast4.gif')
    ]

    def __init__(self, tank_rect):
        super().__init__(Explode.images, tank_rect)
        self.rect.left -= 38
        self.rect.top -= 23

    def display_is(self, window):
        if self.is_live:
            if int(self.state / 20) < len(self.images):
                self.image = self.images[int(self.state / 20)]
                window.blit(self.image, self.rect)
                self.state += 1
                return True
            else:
                return False
        else:
            return False


class Music:
    def __init__(self, filename):
        self.filename = filename
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)

    @staticmethod
    def play():
        pygame.mixer.music.play()


class Set:
    BLOCK = 60
    STEEL = 0
    WALL = 1
    ENEMY = 2
    images = {
        STEEL: pygame.image.load('img/steels.gif'),
        WALL: pygame.image.load('img/wall.gif'),
        ENEMY: pygame.image.load('img/enemy1D.gif')
    }

    def __init__(self, rect):
        self.images = MapElem.images
        self.state = MapElem.STEEL
        self.image = self.images[self.state]
        self.rect = self.image.get_rect()
        self.rect.left = rect.left
        self.rect.top = rect.top
        self.is_live = True


class MapElem(Set):
    def __init__(self, rect):
        super().__init__(rect)

    def display(self, window):
        if self.is_live:
            self.image = self.images[self.state]
            window.blit(self.image, self.rect)
            return True
        else:
            return False

    def move(self, direction):
        if direction == 0 :
            self.rect.top -= MapElem.BLOCK
        elif direction == 1:
            self.rect.top += MapElem.BLOCK
        elif direction == 2:
            self.rect.left -= MapElem.BLOCK
        elif direction == 3:
            self.rect.left += MapElem.BLOCK

    def draw(self, map_list):
        pass
