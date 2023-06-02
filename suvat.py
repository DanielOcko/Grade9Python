import arcade
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Suvat"

class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.CAPRI)

        self.ball1 = Ball(20, 20, 10, 8, 0.4)

    def on_draw(self):
        arcade.start_render()
        self.ball1.draw()
    def on_update(self, delta_time):
        self.ball1.update()

class Ball:

    def __init__(self, x, y, velX, velY, accel):
        self.x = x
        self.y = y
        self.velX = velX
        self.velY = velY
        self.accel = accel
        self.size = 20
        self.color = arcade.color.RED

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

    def update(self):
        self.x += self.velX
        self.y += self.velY
        self.velY -= self.accel

        if self.y < 0:
            self.velY *= -1

Game()
arcade.run()
