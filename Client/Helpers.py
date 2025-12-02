import pyola
import json

class Button:
    def __init__(self, x, y, width, height, text_color=(0, 0, 0), variable=None, color=None, texture=None):
        if (not color and not texture) or (color and texture):
            color = (0.5, 0.5, 0.5)
        if color and not texture:
            self.rect = pyola.shapes.Rectangle(x, y, width, height, color=color)
        self.text_color = text_color
        self.variable = variable

    def draw(self):
        self.rect.draw()

    def is_clicked(self):
        mouse_x, mouse_y = pyola.input.get_mouse_position()
        return pyola.input.collide_pos(self.rect, (mouse_x, mouse_y)) and pyola.input.is_mouse_button_pressed(1)

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)