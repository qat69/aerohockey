import arcade
from constants import *


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.clear()
        arcade.set_background_color(BACKGROUND_COLOR)

        arcade.draw_text("АЭРОХОККЕЙ",
                         SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT - 180,
                         ACCENT_COLOR,
                         64,
                         anchor_x="center",
                         bold=True)

        arcade.draw_text("ДВОЙНОЕ ПРОТИВОСТОЯНИЕ",
                         SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT - 225,
                         TEXT_COLOR,
                         24,
                         anchor_x="center")

        self.draw_button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60, "ИГРАТЬ", 320, 80)
        self.draw_button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60, "ВЫХОД", 320, 80)



        self.draw_hockey_elements()

    def draw_button(self, x, y, text, width, height):
        arcade.draw_lbwh_rectangle_filled(x - width // 2, y - height // 2, width, height, BUTTON_COLOR)
        arcade.draw_lbwh_rectangle_outline(x - width // 2, y - height // 2, width, height, ACCENT_COLOR, 3)
        arcade.draw_text(text, x, y, TEXT_COLOR, 32, anchor_x="center", anchor_y="center")

    def draw_hockey_elements(self):
        arcade.draw_circle_filled(150, 150, 25, PLAYER1_COLOR)
        arcade.draw_circle_filled(SCREEN_WIDTH - 150, 150, 25, PLAYER2_COLOR)

        arcade.draw_line(SCREEN_WIDTH // 2, 70, SCREEN_WIDTH // 2, 230, MENU_COLOR, 2)
        arcade.draw_circle_outline(SCREEN_WIDTH // 2, 150, 60, MENU_COLOR, 2)
        arcade.draw_circle_filled(SCREEN_WIDTH // 2, 150, 20, PUCK_COLOR)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            play_x1 = SCREEN_WIDTH // 2 - 160
            play_x2 = SCREEN_WIDTH // 2 + 160
            play_y1 = SCREEN_HEIGHT // 2 + 60 - 40
            play_y2 = SCREEN_HEIGHT // 2 + 60 + 40

            exit_x1 = SCREEN_WIDTH // 2 - 160
            exit_x2 = SCREEN_WIDTH // 2 + 160
            exit_y1 = SCREEN_HEIGHT // 2 - 60 - 40
            exit_y2 = SCREEN_HEIGHT // 2 - 60 + 40

            if play_x1 <= x <= play_x2 and play_y1 <= y <= play_y2:
                from view.goals_select_view import GoalsSelectView
                select_view = GoalsSelectView()
                self.window.show_view(select_view)

            if exit_x1 <= x <= exit_x2 and exit_y1 <= y <= exit_y2:
                arcade.exit()