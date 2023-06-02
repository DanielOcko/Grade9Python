import arcade
SCREEN_WIDTH =
SCREEN_HEIGHT =
SCREEN_TITLE = " "

class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.###)

    def on_draw(self):
        arcade.start_render()

    def on_update(self, delta_time):
        pass

Game()
arcade.run()
