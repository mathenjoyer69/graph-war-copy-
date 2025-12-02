import pyola

class Player:
    def __init__(self, name, color, pos=(0, 0)):
        self.name = name
        self.color = color
        self.player_box = pyola.shapes.Circle(pos[0], pos[1], 5, color=color)

    def draw(self):
        self.player_box.draw()