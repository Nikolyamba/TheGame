import arcade
from arcade.gui import UIGridLayout, UIAnchorLayout, UIFlatButton, UIView

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

        grid.add(UIFlatButton(text="Начать игру", width=200), row=0, column=0)
        grid.add(UIFlatButton(text="Загрузить игру", width=200), row=1, column=0)
        grid.add(UIFlatButton(text="Сохранить игру", width=200), row=2, column=0)
        grid.add(UIFlatButton(text="Выйти из игры", width=200), row=3, column=0)
