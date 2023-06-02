import arcade
COLUMN_COUNT = 3
ROW_COUNT = 3
WIDTH = 100
HEIGHT = 100
MARGIN = 5
SCREEN_WIDTH = (WIDTH*COLUMN_COUNT)+(MARGIN*(COLUMN_COUNT+1))
SCREEN_HEIGHT = (HEIGHT*ROW_COUNT)+(MARGIN*(ROW_COUNT+1))
SCREEN_TITLE = "Tic Tac Toe"

Empty = 0
O = 1
X = 2

class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.GOLD)
        self.current_player = 2
        self.gameover = False
        self.grid = [[Empty,Empty,Empty],
                     [Empty,Empty,Empty],
                     [Empty,Empty,Empty]]
    def on_draw(self):
        arcade.start_render()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = (WIDTH+MARGIN) * column + MARGIN + WIDTH // 2
                y = (HEIGHT+MARGIN) * row + MARGIN + HEIGHT // 2

                if self.grid[row][column] == Empty:
                    color = arcade.color.RED
                elif self.grid[row][column] == O:
                    color = arcade.color.BLUE
                else:
                    color = arcade.color.GREEN

                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_update(self, delta_time):
        if self.gameover:
            self.close()

    def on_mouse_press(self, x, y, button, modifiers):
        column = int(x//(MARGIN+WIDTH))
        row = int(y//(MARGIN+HEIGHT))

        if self.grid[row][column] is Empty:

            if self.current_player == O:
                self.grid[row][column] = O
                self.current_player = X
            elif self.current_player == X:
                self.grid[row][column] = X
                self.current_player = O

                #Rows
            if self.grid[row] == [O,O,O]:
                print(f"Player {self.current_player} wins!")
                self.gameover = True
            if self.grid[row] == [X,X,X]:
                print(f"Player {self.current_player} wins!")
                self.gameover = True

                #Columns
            if self.grid[0][column] == self.grid[1][column] == self.grid[2][column]:
                print(f"Player {self.current_player} wins!")
                self.gameover = True
            if self.grid[0][column] == self.grid[1][column] == self.grid[2][column]:
                print(f"Player {self.current_player} wins!")
                self.gameover = True

                #Diagonals
            if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] is not Empty:
                print(f"Player {self.current_player} wins!")
                self.gameover = True
            if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] is not Empty:
                print(f"Player {self.current_player} wins!")
                self.gameover = True

            if Empty not in self.grid[0] and Empty not in self.grid[1] and Empty not in self.grid[2]:
                print("Draw. Nobody wins")
                self.gameover = True

Game()
arcade.run()
