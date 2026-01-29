import arcade
from constants import *


class GoalsSelectView(arcade.View):
    def __init__(self):
        super().__init__()
        self.selected_goals = 7

    def on_draw(self):
        self.clear()
        arcade.set_background_color(BACKGROUND_COLOR)

        arcade.draw_text("ВЫБЕРИТЕ КОЛ-ВО ГОЛОВ",
                         SCREEN_WIDTH // 2 + 50,
                         SCREEN_HEIGHT - 180,
                         ACCENT_COLOR,
                         48,
                         anchor_x="center",
                         bold=True)



        self.draw_goal_display()
        self.draw_controls()

    def draw_goal_display(self):
        arcade.draw_lbwh_rectangle_filled(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 120, BUTTON_COLOR)
        arcade.draw_lbwh_rectangle_outline(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 120, ACCENT_COLOR, 3)

        arcade.draw_text(f"{self.selected_goals}",
                         SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT // 2 + 80,
                         ACCENT_COLOR,
                         72,
                         anchor_x="center",
                         anchor_y="center",
                         bold=True)


    def draw_controls(self):
        self.draw_button(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 60, "-", 80, 80)
        self.draw_button(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 2 - 60, "+", 80, 80)

        self.draw_button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 180, "НАЧАТЬ ИГРУ", 400, 80)

        arcade.draw_text("Минимум: 3   Максимум: 10",
                         SCREEN_WIDTH // 2,
                         100,
                         (150, 150, 150),
                         18,
                         anchor_x="center")

    def draw_button(self, x, y, text, width, height):
        arcade.draw_lbwh_rectangle_filled(x - width // 2, y - height // 2, width, height, BUTTON_COLOR)
        arcade.draw_lbwh_rectangle_outline(x - width // 2, y - height // 2, width, height, ACCENT_COLOR, 3)

        if text == "+" or text == "-":
            font_size = 48
        else:
            font_size = 28

        arcade.draw_text(text, x, y, TEXT_COLOR, font_size, anchor_x="center", anchor_y="center")

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            minus_x1 = SCREEN_WIDTH // 2 - 200 - 40
            minus_x2 = SCREEN_WIDTH // 2 - 200 + 40
            minus_y1 = SCREEN_HEIGHT // 2 - 60 - 40
            minus_y2 = SCREEN_HEIGHT // 2 - 60 + 40

            if minus_x1 <= x <= minus_x2 and minus_y1 <= y <= minus_y2:
                if self.selected_goals > 3:
                    self.selected_goals -= 1

            plus_x1 = SCREEN_WIDTH // 2 + 200 - 40
            plus_x2 = SCREEN_WIDTH // 2 + 200 + 40
            plus_y1 = SCREEN_HEIGHT // 2 - 60 - 40
            plus_y2 = SCREEN_HEIGHT // 2 - 60 + 40

            if plus_x1 <= x <= plus_x2 and plus_y1 <= y <= plus_y2:
                if self.selected_goals < 10:
                    self.selected_goals += 1

            start_x1 = SCREEN_WIDTH // 2 - 200
            start_x2 = SCREEN_WIDTH // 2 + 200
            start_y1 = SCREEN_HEIGHT // 2 - 180 - 40
            start_y2 = SCREEN_HEIGHT // 2 - 180 + 40

            if start_x1 <= x <= start_x2 and start_y1 <= y <= start_y2:
                from view.game_view import GameView
                game_view = GameView(max_goals=self.selected_goals)
                self.window.show_view(game_view)