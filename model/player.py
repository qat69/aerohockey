class Player:
    def __init__(self, x, y, color, is_player1=True):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.radius = 30
        self.color = color
        self.dx = 0
        self.dy = 0
        self.move_x = 0
        self.move_y = 0
        self.is_player1 = is_player1

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.dx = 0
        self.dy = 0
        self.move_x = 0
        self.move_y = 0

    def update(self, field_padding, screen_width, screen_height):
        speed = 5
        self.dx = self.move_x * speed
        self.dy = self.move_y * speed

        new_x = self.x + self.dx
        new_y = self.y + self.dy

        new_y = max(field_padding + self.radius,
                    min(screen_height - field_padding - self.radius, new_y))

        center_line = screen_width // 2
        if self.is_player1:
            max_x = center_line - self.radius
            new_x = min(max_x, new_x)
            new_x = max(field_padding + self.radius, new_x)
        else:
            min_x = center_line + self.radius
            new_x = max(min_x, new_x)
            new_x = min(screen_width - field_padding - self.radius, new_x)

        self.x = new_x
        self.y = new_y

    def set_movement(self, dx, dy):
        self.move_x = dx
        self.move_y = dy