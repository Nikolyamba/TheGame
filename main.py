import arcade as arcade

from utils import get_screen_settings
from windows.main_menu_window import MainMenu

def main():
    """Запуск игры, создание меню игры"""
    window = arcade.Window(*get_screen_settings(), fullscreen=False)
    main_menu_settings = MainMenu()
    window.show_view(main_menu_settings)
    arcade.run()

if __name__ == "__main__":
    main()