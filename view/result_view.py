import arcade
from constants import *


class ResultView(arcade.View):
    def __init__(self, winner, max_goals):
        super().__init__()
        self.winner = winner
        self.max_goals = max_goals

    def on_draw(self):
        self.clear()
        arcade.set_background_color(BACKGROUND_COLOR)

        arcade.draw_text("ИГРА ЗАВЕРШЕНА",
                         SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT - 180,
                         ACCENT_COLOR,
                         48,
                         anchor_x="center",
                         bold=True)

        if self.winner == 1:
            color = PLAYER1_COLOR
            text = "ИГРОК 1 ПОБЕДИЛ!"
            subtext = "Синяя команда одержала победу"
        else:
            color = PLAYER2_COLOR
            text = "ИГРОК 2 ПОБЕДИЛ!"
            subtext = "Красная команда одержала победу"

        arcade.draw_text(text,
                         SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT // 2 + 80,
                         color,
                         56,
                         anchor_x="center",
                         bold=True)

        arcade.draw_text(subtext,
                         SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT // 2 + 30,
                         TEXT_COLOR,
                         22,
                         anchor_x="center")

        arcade.draw_text(f"Лимит матча: {self.max_goals} голов",
                         SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT // 2 - 20,
                         (180, 180, 180),
                         20,
                         anchor_x="center")

        self.draw_button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120, "ВЕРНУТЬСЯ В МЕНЮ", 450, 80)



    def draw_button(self, x, y, text, width, height):
        arcade.draw_lbwh_rectangle_filled(x - width // 2, y - height // 2, width, height, BUTTON_COLOR)
        arcade.draw_lbwh_rectangle_outline(x - width // 2, y - height // 2, width, height, ACCENT_COLOR, 3)
        arcade.draw_text(text, x, y, TEXT_COLOR, 28, anchor_x="center", anchor_y="center")






    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            btn_x1 = SCREEN_WIDTH // 2 - 225
            btn_x2 = SCREEN_WIDTH // 2 + 225
            btn_y1 = SCREEN_HEIGHT // 2 - 120 - 40
            btn_y2 = SCREEN_HEIGHT // 2 - 120 + 40

            if btn_x1 <= x <= btn_x2 and btn_y1 <= y <= btn_y2:
                from view.menu_view import MenuView
                self.window.show_view(MenuView())