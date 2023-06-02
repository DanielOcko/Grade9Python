import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Plat-latter"

CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 6
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

LEFT_VIEWPOINT_MARGIN = 250
RIGHT_VIEWPOINT_MARGIN = 250
TOP_VIEWPOINT_MARGIN = 50
BOTTOM_VIEWPOINT_MARGIN = 60


class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMBER)

        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.player_sprite = None

        self.view_bottom = 0
        self.view_left = 0

        self.score = 0

        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump3.wav")


    def setup(self):

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.num_jumps = 0

        image_source = ":resources:images/animated_characters/robot/robot_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        map_name = 'map.tmx'
        platforms_layer_name = 'Platforms'
        coins_layer_name = 'Coins'
        decorations_layer_name = 'Decorations'

        my_map = arcade.tilemap.read_tmx(map_name)

        self.wall_list = arcade.tilemap.process_layer(map_object = my_map,
                                                      layer_name = platforms_layer_name,
                                                      scaling = TILE_SCALING,
                                                      use_spatial_hash = True)

        self.coin_list = arcade.tilemap.process_layer(my_map, coins_layer_name, TILE_SCALING)

        self.decorations_list = arcade.tilemap.process_layer(my_map, decorations_layer_name, TILE_SCALING)

        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)


        # for x in range(0, 1250, 64):
        #     wall = arcade.Sprite(":resources:images/tiles/dirtMid.png", TILE_SCALING)
        #     wall.center_x = x
        #     wall.center_y = 32
        #     self.wall_list.append(wall)
        #
        # coordinate_list = [[512, 96], [256, 96], [768, 96]]
        #
        # for coordinate in coordinate_list:
        #     wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
        #     wall.position = coordinate
        #     self.wall_list.append(wall)
        #
        # for x in range(200, 1200, 250):
        #     coin = arcade.Sprite(":resources:images/items/coinGold.png", COIN_SCALING)
        #     coin.center_x = x
        #     coin.center_y = 96
        #     self.coin_list.append(coin)

        self.obstruct = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                       self.wall_list,
                                                       GRAVITY)

    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()
        self.coin_list.draw()
        self.decorations_list.draw()
        self.player_list.draw()

        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10+self.view_left, 610+self.view_bottom,
                                                       arcade.color.WHITE, 18)

    def on_update(self, delta_time):

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)
            self.score += 1

        self.obstruct.update()

        changed = False

        left_boundary = self.view_left + LEFT_VIEWPOINT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPOINT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPOINT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        bottom_boundary = self.view_bottom + BOTTOM_VIEWPOINT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)




    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            if self.obstruct.can_jump():
                self.num_jumps = 0
            if self.num_jumps < 2:
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                self.num_jumps += 1
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0


def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()


Game()
arcade.run()
