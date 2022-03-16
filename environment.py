from tkinter import Canvas


class Environment:
    def __init__(self, fight_map: Canvas):
        self.fight_map = fight_map

    def can_move(self, position_x: int, position_y: int, direction: str, speed: int):
        return (position_x, position_y) != self.get_next_position(
            position_x, position_y, direction, speed)

    def get_next_position(self, position_x: int, position_y: int, direction: str, speed: int) \
            -> (int, int):
        if position_x < 1000 and direction == "right":
            position_x += speed
            if position_x > 1000:
                position_x = 1000
        elif position_x > 0 and direction == "left":
            position_x -= speed
            if position_x < 0:
                position_x = 0
        elif position_y > 0 and direction == "up":
            position_y -= speed
            if position_y < 0:
                position_y = 0
        elif position_y < 1000 and direction == "down":
            position_y += speed
            if position_y > 1000:
                position_y = 1000
        return position_x, position_y
