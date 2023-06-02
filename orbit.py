import arcade
import math
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Orbit Simulation"
sun_size = 75
class Planet:
    def __init__(self, size, orb_vel, orb_rad, color):
        self.size = size
        self.orb_vel = orb_vel
        self.orb_rad = orb_rad
        self.color = color

        self.x = SCREEN_WIDTH/2
        self.y = (SCREEN_HEIGHT/2) - orb_rad
        self.angle = 270

    def planet_update(self):
        self.angle = self.angle + self.orb_vel
        self.y = self.orb_rad * math.sin(math.radians(self.angle)) + SCREEN_HEIGHT/2
        self.x = self.orb_rad * math.cos(math.radians(self.angle)) + SCREEN_WIDTH/2

class Simulation(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.planets = []
        self.mercury = Planet(10, 10, 20 + sun_size, arcade.color.BEAVER)
        self.planets.append(self.mercury)
        self.venus = Planet(20, 8, 45 + sun_size, arcade.color.BURLYWOOD)
        self.planets.append(self.venus)
        self.earth = Planet(30, 6, 70 + sun_size, arcade.color.BLUEBONNET)
        self.planets.append(self.earth)
        self.mars = Planet(20, 4, 95 + sun_size, arcade.color.CARNELIAN)
        self.planets.append(self.mars)
        self.jupiter = Planet(80, 0.5, 195 + sun_size, arcade.color.CAMEL)
        self.planets.append(self.jupiter)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, sun_size, arcade.color.ORANGE)
        for planet in self.planets:
            arcade.draw_circle_filled(planet.x,
                                      planet.y,
                                      planet.size,
                                      planet.color)

    def on_update(self, delta_time):
        for planet in self.planets:
            planet.planet_update()

Simulation()
arcade.run()
