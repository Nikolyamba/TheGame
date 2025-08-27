from typing import Tuple

import arcade
from screeninfo import get_monitors

def get_screen_settings() -> Tuple[int, int, str]:
    """Функция получает информацию о разрешении экрана пользователя"""
    width = 0
    height = 0
    for monitor in get_monitors():
        width = monitor.width
        height = monitor.height
    return width, height, "DoubleKGames"
