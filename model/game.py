import arcade
import math
from .player import Player
from .puck import Puck
from constants import *


class Game:
    def __init__(self, max_goals=7):
        self.player1 = Player(SCREEN_WIDTH * 0.25, SCREEN_HEIGHT // 2, PLAYER1_COLOR, is_player1=True)
        self.player2 = Player(SCREEN_WIDTH * 0.75, SCREEN_HEIGHT // 2, PLAYER2_COLOR, is_player1=False)
        self.puck = Puck(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.score1 = 0
        self.score2 = 0
        self.max_goals = max_goals
        self.game_over = False
        self.winner = None

    def update(self):
        if self.game_over:
            return

        self.player1.update(FIELD_PADDING, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.player2.update(FIELD_PADDING, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.puck.update()

        self.puck.check_wall_collision(FIELD_PADDING, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.check_player_collision(self.player1)
        self.check_player_collision(self.player2)

        self.check_goals()

    def check_player_collision(self, player):
        dx = self.puck.x - player.x
        dy = self.puck.y - player.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < self.puck.radius + player.radius:
            angle = math.atan2(dy, dx)

            base_force = 12

            player_speed = (player.dx ** 2 + player.dy ** 2) ** 0.5
            speed_bonus = player_speed * 3

            direction_bonus = 0
            if player.is_player1 and dx > 0:
                direction_bonus = 4
            elif not player.is_player1 and dx < 0:
                direction_bonus = 4

            total_force = base_force + speed_bonus + direction_bonus
            total_force = min(total_force, 25)

            self.puck.dx = math.cos(angle) * total_force
            self.puck.dy = math.sin(angle) * total_force

    def check_goals(self):
        if self.puck.x < FIELD_PADDING:
            goal_top = SCREEN_HEIGHT // 2 + GOAL_WIDTH // 2
            goal_bottom = SCREEN_HEIGHT // 2 - GOAL_WIDTH // 2

            if goal_bottom < self.puck.y < goal_top:
                self.score2 += 1
                self.reset_positions()
                return

        if self.puck.x > SCREEN_WIDTH - FIELD_PADDING:
            goal_top = SCREEN_HEIGHT // 2 + GOAL_WIDTH // 2
            goal_bottom = SCREEN_HEIGHT // 2 - GOAL_WIDTH // 2

            if goal_bottom < self.puck.y < goal_top:
                self.score1 += 1
                self.reset_positions()
                return

        if self.score1 >= self.max_goals or self.score2 >= self.max_goals:  # ИСПРАВЛЕНО
            self.game_over = True
            self.winner = 1 if self.score1 > self.score2 else 2

    def reset_positions(self):
        self.puck.reset()
        self.player1.reset()
        self.player2.reset()

    def move_player1(self, key, pressed):
        dx, dy = 0, 0

        if pressed.get(arcade.key.W, False):
            dy += 1
        if pressed.get(arcade.key.S, False):
            dy -= 1
        if pressed.get(arcade.key.A, False):
            dx -= 1
        if pressed.get(arcade.key.D, False):
            dx += 1

        if dx != 0 and dy != 0:
            length = (dx ** 2 + dy ** 2) ** 0.5
            dx /= length
            dy /= length

        self.player1.set_movement(dx, dy)

    def move_player2(self, key, pressed):
        dx, dy = 0, 0

        if pressed.get(arcade.key.UP, False):
            dy += 1
        if pressed.get(arcade.key.DOWN, False):
            dy -= 1
        if pressed.get(arcade.key.LEFT, False):
            dx -= 1
        if pressed.get(arcade.key.RIGHT, False):
            dx += 1

        if dx != 0 and dy != 0:
            length = (dx ** 2 + dy ** 2) ** 0.5
            dx /= length
            dy /= length

        self.player2.set_movement(dx, dy)