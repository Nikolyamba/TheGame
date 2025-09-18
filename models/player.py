import arcade

from utils import get_screen_settings

class Player(arcade.Sprite):
    def __init__(self, image_path="sprites/back.jpg", scale=0.5):
        super().__init__(image_path, scale)

        self.move_speed = 5
        self.run_speed = 10
        self.movement_speed = self.move_speed

        self.stamina = 100
        self.stamina_recovery = 5
        self.stamina_usage = 5
        self.is_running = False

        self.wood_values = 0
        self.metal_values = 0
        self.food_values = 0
        self.player_weight = 0

        self.textures_dict = {
            "up": arcade.load_texture("sprites/back.jpg"),
            "down": arcade.load_texture("sprites/back.jpg"),
            "left": arcade.load_texture("sprites/left.jpg"),
            "right": arcade.load_texture("sprites/right.jpg")
        }

        self.texture = self.textures_dict["up"]

        self.window_width = get_screen_settings()[0]
        self.window_height = get_screen_settings()[1]

    def update(self, delta_time: float = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.stamina >= 5 and self.is_running:
            self.stamina -= self.stamina_usage * delta_time
            self.movement_speed = self.run_speed
        else:
            self.stamina += self.stamina_recovery * delta_time
            self.movement_speed = self.move_speed

        if self.left < 0:
            self.left = 0
        elif self.right > self.window_width - 1:
            self.right = self.window_width - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > self.window_height - 1:
            self.top = self.window_height - 1