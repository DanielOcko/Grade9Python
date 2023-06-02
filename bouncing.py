import arcade
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bouncing Balls"

class Ball:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.change_x = random.randint(1, 5)
        self.change_y = random.randint(1, 5)
        self.size = random.randint(10, 15)
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))

class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color((random.randint(0, 255),
                                     random.randint(0, 255),
                                     random.randint(0, 255)))

        self.ball_list = []
        new_ball = Ball()
        self.ball_list.append(new_ball)

    def on_draw(self):
        arcade.start_render()

        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)

    def on_update(self, delta_time):
        for ball in self.ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.x < ball.size:
                ball.change_x *= -1
            elif ball.x > SCREEN_WIDTH-ball.size:
                ball.change_x = random.randint(-5, -1)

            if ball.y < ball.size:
                ball.change_y *= -1
            elif ball.y > SCREEN_HEIGHT-ball.size:
                ball.change_y = random.randint(-5, -1)
Game()
arcade.run()
