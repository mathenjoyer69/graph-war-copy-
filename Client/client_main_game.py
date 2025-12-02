import time
from Client.Player import Player
from Client.Helpers import *


class ClientMainGame:
    def __init__(self, width=800, height=600):
        self.win = pyola.window.Window(width, height, "Client Game")
        self.grid_lines = [(width/2, 15), (width/2, 450+15), (15, (450+15)/2), (width-15, (450+15)/2)]
        self.game_win = pyola.shapes.Rectangle(15, 15, 770, 450, color=(0.8, 0.8, 0.8))
        self.players = []
        self.user_data: dict = load_json('Client/client_info.json')

    def update(self):
        self.win.update()

    def draw(self, surface):
        self.game_win.draw()
        for i in range(0, len(self.grid_lines), 2):
            pyola.shapes.Line(self.grid_lines[i], self.grid_lines[i+1], color=(0, 0, 0)).draw()

        if self.players:
            for player in self.players:
                player.draw()

    def spawn_player(self, name, color, pos):
        self.players.append(Player(name, color, pos))

    def run(self):
        while self.win.running:
            pyola.renderer.clear((0.2, 0.2, 0.2))
            mouse_x, mouse_y = pyola.input.get_mouse_position()
            if pyola.input.is_mouse_button_pressed(1):
                self.spawn_player(self.user_data['name'], tuple(self.user_data['color']), (mouse_x, mouse_y))

            self.draw(self.win)
            self.update()
            time.sleep(1 / 60)

        self.win.close()