import math


class Puck:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.radius = 20
        self.dx = 0
        self.dy = 0

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.dx = 0
        self.dy = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.dx *= 0.98
        self.dy *= 0.98

        if abs(self.dx) < 0.05:
            self.dx = 0
        if abs(self.dy) < 0.05:
            self.dy = 0

    def check_wall_collision(self, field_padding, screen_width, screen_height):
        if self.y - self.radius < field_padding:
            self.y = field_padding + self.radius
            self.dy *= -1
        elif self.y + self.radius > screen_height - field_padding:
            self.y = screen_height - field_padding - self.radius
            self.dy *= -1

        goal_top = screen_height // 2 + 100
        goal_bottom = screen_height // 2 - 100

        if self.x - self.radius < field_padding:
            if not (goal_bottom < self.y < goal_top):
                self.x = field_padding + self.radius
                self.dx *= -1

        if self.x + self.radius > screen_width - field_padding:
            if not (goal_bottom < self.y < goal_top):
                self.x = screen_width - field_padding - self.radius
                self.dx *= -1