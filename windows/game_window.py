import arcade
from arcade.gui import UIView

from models.player import Player

class GameWindow(UIView):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.PINK
        self.player_list = None
        self.player_sprite = None

    def setup(self):

        self.player_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        self.clear()
        self.player_list.draw()

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            from windows.main_menu_window import MainMenu
            self.window.show_view(MainMenu())
        elif key == arcade.key.W:
            self.player_sprite.change_y = self.player_sprite.movement_speed
        elif key == arcade.key.S:
            self.player_sprite.change_y = -self.player_sprite.movement_speed
        elif key == arcade.key.A:
            self.player_sprite.change_x = -self.player_sprite.movement_speed
        elif key == arcade.key.D:
            self.player_sprite.change_x = self.player_sprite.movement_speed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
