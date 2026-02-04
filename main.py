import arcade
from view.menu_view import MenuView
from constants import Constants


class AirHockeyWindow(arcade.Window):
    def init(self):
        super().__init__(Constants.screen_width, Constants.screen_height, Constants.screen_title)
        self.show_view(MenuView())


def main():
    music = arcade.Sound("dist/assets/sounds/menu.mp3")
    music.play(volume=0.5, loop=True)
    window = AirHockeyWindow()
    arcade.run()


if __name__ == "main":
    main()