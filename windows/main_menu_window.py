import arcade
from arcade.gui import UIGridLayout, UIAnchorLayout, UIFlatButton, UIView

from windows.game_window import GameWindow

class MainMenu(UIView):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.PINK

        grid = UIGridLayout(
            column_count=3,
            row_count=4,
            size_hint=(0, 0),
            vertical_spacing=10,
            horizontal_spacing=10,
        )

        self.ui.add(UIAnchorLayout(children=[grid]))

        exit_button = UIFlatButton(text="Выйти из игры", width=200)
        start_button = UIFlatButton(text="Начать игру", width=200)

        grid.add(start_button, row=0, column=0)
        grid.add(UIFlatButton(text="Загрузить игру", width=200), row=1, column=0)
        grid.add(UIFlatButton(text="Сохранить игру", width=200), row=2, column=0)
        grid.add(exit_button, row=3, column=0)

        @exit_button.event("on_click")
        def on_click_exit(event):
            arcade.exit()

        @start_button.event("on_click")
        def on_click_start(event):
            self.window.show_view(GameWindow())
