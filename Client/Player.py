import pyola
import numpy as np

class Player:
    def __init__(self, name, color, pos=(0, 0)):
        self.name = name
        self.color = color
        self.player_box = pyola.shapes.Circle(pos[0], pos[1], 5, color=color)
        self.pos = pos

    def draw(self):
        self.player_box.draw()

    def draw_function(self, func, max_points=1000):
        x_values = np.linspace(0, max_points, max_points)+self.pos[0]
        y_values = func(x_values)+self.pos[1]
        points = [(x, y) for x, y in zip(x_values, y_values)]
        for i in range(len(points)-1):
            pyola.shapes.Line(points[i], points[i+1], color=self.color).draw()
        return points
