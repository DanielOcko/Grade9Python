import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Particle Simulation"

class Particle:
    def __init__(self, size, x, y, color, movespeed_x, movespeed_y):
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.movespeed_x = movespeed_x
        self.movespeed_y = movespeed_y

    def update(self):
        self.x += self.movespeed_x
        self.y += self.movespeed_y

        if self.x < self.size:
            self.movespeed_x *= -1
        elif self.x > SCREEN_WIDTH-self.size:
            self.movespeed_x *= -1

        if self.y < self.size:
            self.movespeed_y *= -1
        elif self.y > SCREEN_HEIGHT-self.size:
            self.movespeed_y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

class Neutron(Particle):
    def __init__(self, x, y):
        super().__init__(5, x, y, arcade.color.DIAMOND, 10, 10)

class Fuel_Atom(Particle):
    def __init__(self, x, y):
        super().__init__(20, x, y, arcade.color.GREEN, 3, 3)

class Daughter_Atom(Particle):
    def __init__(self, x, y):
        super().__init__(10, x, y, arcade.color.PINK, 5, 5)


class Reactor(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)
        self.neutron_list = []
        self.fuelAtom_list = []
        self.daughterAtom_list = []

    def on_draw(self):
        arcade.start_render()
        for neutron in self.neutron_list:
            neutron.draw()
        for fuel_atom in self.fuelAtom_list:
            fuel_atom.draw()
        for daughter_atom in self.daughterAtom_list:
            daughter_atom.draw()

    def on_update(self, delta_time):
        for neutron in self.neutron_list:
            neutron.update()
        for fuel_atom in self.fuelAtom_list:
            fuel_atom.update()
        for daughter_atom in self.daughterAtom_list:
            daughter_atom.update()
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            neutron = Neutron(x, y)
            self.neutron_list.append(neutron)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            fuel_atom = Fuel_Atom(x, y)
            self.fuelAtom_list.append(fuel_atom)

Reactor()
arcade.run()
