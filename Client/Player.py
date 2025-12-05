import pyola
import numpy as np
import Client.Helpers

settings = Client.Helpers.load_json("settings.json")

class Player:
    def __init__(self, name, color, pos=(0, 0)):
        self.name = name
        self.color = color
        self.player_box = pyola.shapes.Circle(pos[0], pos[1], 5, color=color)
        self.pos = pos
        self.hit_object = False

    def draw(self):
        self.player_box.draw()

    def draw_function(self, func, multi, axis_x0, max_points=2000):
        screen_min_x = 15
        screen_max_x = settings['graph_width'] + 15
        screen_min_y = 15
        screen_max_y = settings['graph_height'] + 15
        t = np.linspace(0, screen_max_x, max_points)
        x_screen = self.pos[0] + t

        x_math = x_screen - axis_x0
        y_values = func(x_math, multi)

        x_values = x_screen
        y_values = -y_values + self.pos[1] + y_values[0]

        points = list(zip(x_values, y_values))
        for i in range(len(points)-1):
            x = x_values[i]
            y = y_values[i]
            if x < screen_min_x or x > screen_max_x:
                self.hit_object = True
                break

            if y < screen_min_y or y > screen_max_y:
                self.hit_object = True
                break

            pyola.shapes.Line(points[i], points[i+1], color=self.color).draw()


        return points

    def reset_player(self):
        pass
