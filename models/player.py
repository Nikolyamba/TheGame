import arcade

from utils import get_screen_settings

class Player(arcade.Sprite):
    def __init__(self, image_path="sprites/player.png", scale=0.5):
        super().__init__(image_path, scale)
        self.movement_speed = 5
        self.window_width = get_screen_settings()[0]
        self.window_height = get_screen_settings()[1]

    def update(self, delta_time: float = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > self.window_width - 1:
            self.right = self.window_width - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > self.window_height - 1:
            self.top = self.window_height - 1