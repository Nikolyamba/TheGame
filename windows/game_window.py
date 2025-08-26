import arcade
from arcade.gui import UIView

class GameWindow(UIView):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.PINK

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            from windows.main_menu_window import MainMenu
            self.window.show_view(MainMenu())