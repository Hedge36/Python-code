class Rect:
    def __init__(self, left: int, top: int):
        self.left = left
        self.top = top


def is_collision_rect(obj_1, obj_2):
    # 此处的对象要求是get_rect返回的对象
    a = obj_1.left - obj_2.left
    b = obj_1.top - obj_2.top
    if obj_2.width > a > -obj_1.width:
        if obj_2.height > b > -obj_1.height:
            return True
        else:
            return False
    else:
        return False
