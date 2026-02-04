import arcade
from view.menu_view import MenuView
from constants import Constants


class AirHockeyWindow(arcade.Window):
    def init(self):
        super().__init__(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, Constants.SCREEN_TITLE)
        self.show_view(MenuView())


def main():
    music = arcade.Sound("dist/assets/sounds/menu.mp3")
    music.play(volume=0.5, loop=True)
    window = AirHockeyWindow()
    arcade.run()


if __name__ == "main":
    main()