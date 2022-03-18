from tkinter import Canvas


class Environment:
    def __init__(self, fight_map: Canvas):
        self.fight_map = fight_map
        self.jack_position_x = int
        self.jack_position_y = int
        self.enemy_position_x = int
        self.enemy_position_y = int
        self.all_top_jack_position_x = []
        self.all_top_enemy_position_x = []

    def can_move(self, position_x: int, position_y: int, direction: str, speed: int):
        return (position_x, position_y) != self.get_next_position(
            position_x, position_y, direction, speed)

    def get_next_position(self, position_x: int, position_y: int, direction: str, speed: int) \
            -> (int, int):
        if position_x < 710 and direction == "right":
            position_x += speed
            if position_x > 710:
                position_x = 710
        elif position_x > 0 and direction == "left":
            position_x -= speed
            if position_x < 0:
                position_x = 0
        elif position_y > 0 and direction == "up":
            position_y -= speed
            if position_y < 0:
                position_y = 0
        elif position_y < 420 and direction == "down":
            position_y += speed
            if position_y > 420:
                position_y = 420
        return position_x, position_y

    def get_postion_all_Player(self, name, position_x, position_y):
        if name == "Jack":
            self.all_top_jack_position_x = [
                                            # Top (x, y)
                                            (position_x, position_y),
                                            (position_x + 10, position_y),
                                            (position_x + 20, position_y),
                                            (position_x + 30, position_y),
                                            (position_x + 40, position_y),
                                            (position_x + 50, position_y),
                                            (position_x + 60, position_y),
                                            (position_x + 70, position_y),
                                            (position_x + 80, position_y),
                                            # Down
                                            (position_x, position_y + 80),
                                            (position_x + 10, position_y + 80),
                                            (position_x + 20, position_y + 80),
                                            (position_x + 30, position_y + 80),
                                            (position_x + 40, position_y + 80),
                                            (position_x + 50, position_y + 80),
                                            (position_x + 60, position_y + 80),
                                            (position_x + 70, position_y + 80),
                                            # Left
                                            (position_x, position_y + 10),
                                            (position_x, position_y + 20),
                                            (position_x, position_y + 30),
                                            (position_x, position_y + 40),
                                            (position_x, position_y + 50),
                                            (position_x, position_y + 60),
                                            (position_x, position_y + 70),
                                            (position_x, position_y + 80),
                                            # Right
                                            (position_x + 80, position_y + 10),
                                            (position_x + 80, position_y + 20),
                                            (position_x + 80, position_y + 30),
                                            (position_x + 80, position_y + 40),
                                            (position_x + 80, position_y + 50),
                                            (position_x + 80, position_y + 60),
                                            (position_x + 80, position_y + 70),
                                            (position_x + 80, position_y + 80),
                                            ]

        elif name == "enemy":
            self.all_top_enemy_position_x = [
                                             (position_x, position_y),
                                             (position_x + 10, position_y + 10),
                                             (position_x + 20, position_y + 20),
                                             (position_x + 30, position_y + 30),
                                             (position_x + 40, position_y + 40),
                                             (position_x + 50, position_y + 50),
                                             (position_x + 60, position_y + 60),
                                             (position_x + 70, position_y + 70),
                                             (position_x + 80, position_y + 80),
                                             (position_x, position_y + 80),
                                             (position_x + 10, position_y + 80),
                                             (position_x + 20, position_y + 80),
                                             (position_x + 30, position_y + 80),
                                             (position_x + 40, position_y + 80),
                                             (position_x + 50, position_y + 80),
                                             (position_x + 60, position_y + 80),
                                             (position_x + 70, position_y + 80),
                                             # Left
                                             (position_x, position_y + 10),
                                             (position_x, position_y + 20),
                                             (position_x, position_y + 30),
                                             (position_x, position_y + 40),
                                             (position_x, position_y + 50),
                                             (position_x, position_y + 60),
                                             (position_x, position_y + 70),
                                             (position_x, position_y + 80),
                                             # Right
                                             (position_x + 80, position_y + 10),
                                             (position_x + 80, position_y + 20),
                                             (position_x + 80, position_y + 30),
                                             (position_x + 80, position_y + 40),
                                             (position_x + 80, position_y + 50),
                                             (position_x + 80, position_y + 60),
                                             (position_x + 80, position_y + 70),
                                             (position_x + 80, position_y + 80),
                                             ]

        same_position = []

        for position in self.all_top_jack_position_x:
            if position in self.all_top_enemy_position_x:
                same_position.append(position)

        if same_position:
            print("Same position : ", position)
            same_position.clear()
        else:
            pass
