import arcade
from model.game import Game
from constants import *


class GameView(arcade.View):
    def __init__(self, max_goals=7):
        super().__init__()
        self.game = Game(max_goals=max_goals)
        self.max_goals = max_goals

        self.keys_pressed = {
            arcade.key.W: False,
            arcade.key.S: False,
            arcade.key.A: False,
            arcade.key.D: False,

            arcade.key.UP: False,
            arcade.key.DOWN: False,
            arcade.key.LEFT: False,
            arcade.key.RIGHT: False,
        }

    def on_show_view(self):
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        self.clear()
        self.draw_field()
        self.draw_players()
        self.draw_score()
        self.draw_half_restrictions()

    def draw_field(self):
        arcade.draw_lbwh_rectangle_filled(FIELD_PADDING,
                                          FIELD_PADDING,
                                          SCREEN_WIDTH - 2 * FIELD_PADDING,
                                          SCREEN_HEIGHT - 2 * FIELD_PADDING,
                                          FIELD_COLOR)

        arcade.draw_line(SCREEN_WIDTH // 2, FIELD_PADDING,
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT - FIELD_PADDING,
                         LINE_COLOR, 2)

        arcade.draw_circle_outline(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                   80, LINE_COLOR, 2)

        arcade.draw_lbwh_rectangle_filled(0,
                                          SCREEN_HEIGHT // 2 - GOAL_WIDTH // 2,
                                          FIELD_PADDING,
                                          GOAL_WIDTH,
                                          arcade.color.BLACK)

        arcade.draw_lbwh_rectangle_filled(SCREEN_WIDTH - FIELD_PADDING,
                                          SCREEN_HEIGHT // 2 - GOAL_WIDTH // 2,
                                          FIELD_PADDING,
                                          GOAL_WIDTH,
                                          arcade.color.BLACK)

        left = FIELD_PADDING
        right = SCREEN_WIDTH - FIELD_PADDING
        top = SCREEN_HEIGHT - FIELD_PADDING
        bottom = FIELD_PADDING

        arcade.draw_line(left, top, right, top, LINE_COLOR, 2)
        arcade.draw_line(left, bottom, right, bottom, LINE_COLOR, 2)

        goal_y_top = SCREEN_HEIGHT // 2 + GOAL_WIDTH // 2
        goal_y_bottom = SCREEN_HEIGHT // 2 - GOAL_WIDTH // 2
        arcade.draw_line(FIELD_PADDING, goal_y_top,
                         FIELD_PADDING, goal_y_bottom,
                         LINE_COLOR, 2)

        arcade.draw_line(SCREEN_WIDTH - FIELD_PADDING, goal_y_top,
                         SCREEN_WIDTH - FIELD_PADDING, goal_y_bottom,
                         LINE_COLOR, 2)

    def draw_half_restrictions(self):
        center_x = SCREEN_WIDTH // 2

        arcade.draw_lbwh_rectangle_filled(
            center_x,
            FIELD_PADDING,
            SCREEN_WIDTH - FIELD_PADDING - center_x,
            SCREEN_HEIGHT - 2 * FIELD_PADDING,
            (100, 100, 255, 50)
        )

        arcade.draw_lbwh_rectangle_filled(
            FIELD_PADDING,
            FIELD_PADDING,
            center_x - FIELD_PADDING,
            SCREEN_HEIGHT - 2 * FIELD_PADDING,
            (255, 100, 100, 50)
        )

    def draw_players(self):
        p1 = self.game.player1
        p2 = self.game.player2
        puck = self.game.puck

        arcade.draw_circle_filled(p1.x, p1.y, p1.radius, p1.color)
        arcade.draw_circle_filled(p2.x, p2.y, p2.radius, p2.color)
        arcade.draw_circle_filled(puck.x, puck.y, puck.radius, PUCK_COLOR)

    def draw_score(self):
        score_text = f"{self.game.score1} : {self.game.score2}"
        arcade.draw_text(score_text,
                         SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT - 40,
                         TEXT_COLOR,
                         36,
                         anchor_x="center",
                         bold=True)

        limit_text = f"Игра до {self.max_goals} голов"
        arcade.draw_text(limit_text,
                         SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT - 80 + 15,
                         arcade.color.DARK_GRAY,
                         16,
                         anchor_x="center")

        controls_text = "Игрок 1: WASD - движение"
        arcade.draw_text(controls_text,
                         20,
                         45,
                         arcade.color.DARK_GRAY,
                         12)

        controls_text2 = "Игрок 2: Стрелки - движение"
        arcade.draw_text(controls_text2,
                         20,
                         30,
                         arcade.color.DARK_GRAY,
                         12)

        esc_text = "ESC - меню"
        arcade.draw_text(esc_text,
                         20,
                         15,
                         arcade.color.DARK_GRAY,
                         12)

    def on_update(self, delta_time):
        self.game.move_player1(None, self.keys_pressed)
        self.game.move_player2(None, self.keys_pressed)

        self.game.update()
        if self.game.game_over:
            from view.result_view import ResultView
            self.window.show_view(ResultView(self.game.winner, self.max_goals))

    def on_key_press(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed[key] = True

        if key == arcade.key.ESCAPE:
            from view.menu_view import MenuView
            self.window.show_view(MenuView())

    def on_key_release(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed[key] = False