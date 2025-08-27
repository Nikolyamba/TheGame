from typing import Tuple

import arcade
from screeninfo import get_monitors

def get_screen_settings() -> Tuple[int, int, str]:
    """Функция получает информацию о разрешении экрана пользователя"""
    monitors = get_monitors()
    if monitors:
        monitor = monitors[0]
        width = monitor.width
        height = monitor.height
    else:
        width = height = 0
    return width, height, "DoubleKGames"
