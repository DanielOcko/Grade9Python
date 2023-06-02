import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Stopwatch Program"

class stopWatch(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.total_time = 0
    def setup(self):
        arcade.set_background_color(arcade.color.DIAMOND)

    def on_draw(self):
        arcade.start_render()
        text = f"Time Elapsed: {self.total_time}"
        arcade.dra

    def on_update(self, delta_time):
        self.total_time += delta_time


stopwatch = stopWatch()
stopwatch.setup()
arcade.run()
