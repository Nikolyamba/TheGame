import arcade as arcade

from screeninfo import get_monitors
from typing import Tuple

from TheGame.windows.main_menu import MainMenu

def get_screen_settings() -> Tuple[int, int]:
    """Функция получает информацию о разрешении экрана пользователя"""
    width = 0
    height = 0
    for monitor in get_monitors():
        width = monitor.width
        height = monitor.height
    return width, height

def main():
    window = arcade.Window(*get_screen_settings(), "DoubleKGames")
    main_menu = MainMenu()  # создаём объект меню
    window.show_view(main_menu)  # показываем меню
    arcade.run()

if __name__ == "__main__":
    main()