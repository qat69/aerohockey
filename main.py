import arcade
from view.menu_view import MenuView
from constants import *

class AirHockeyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.show_view(MenuView())



def main():
    music = arcade.Sound("assets/sounds/menu.mp3")
    music.play(volume=1.0, loop=True)
    window = AirHockeyWindow()
    arcade.run()


if __name__ == "__main__":
    main()