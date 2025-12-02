import pyola
import json
import numpy as np
import glfw

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

def test_function(x, multiplier):
    return multiplier*np.sin(x/multiplier)

class Entry:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.base_color = (130/255, 130/255, 130/255)
        self.active_color = (170/255, 170/255, 170/255)
        self.entry_rect = pyola.shapes.Rectangle(x, y, width, height)
        self.text = ''
        self.active = False
        self.was_pressed = False
        self.last_keys = set()

    def draw(self):
        color = self.active_color if self.active else self.base_color
        self.entry_rect.color = color
        self.entry_rect.draw()

    def handle_event(self):
        mx, my = pyola.input.get_mouse_position()
        now_pressed = pyola.input.is_mouse_button_pressed(glfw.MOUSE_BUTTON_LEFT)

        if pyola.input.collide_pos(self.entry_rect, (mx, my)):
            if now_pressed and not self.was_pressed:
                self.active = not self.active  # toggle only once when click starts

        self.was_pressed = now_pressed  # store current state for next frame

    def handle_keyboard(self):
        if not self.active:
            return

        if pyola.input.is_key_pressed(glfw.KEY_BACKSPACE):
            if glfw.KEY_BACKSPACE not in self.last_keys:
                self.text = self.text[:-1]

        if pyola.input.is_key_pressed(glfw.KEY_ENTER):
            if glfw.KEY_ENTER not in self.last_keys:
                self.active = False

        for char in pyola.input.get_typed_chars():
            self.text += char

        self.last_keys = {
            key for key in [glfw.KEY_BACKSPACE, glfw.KEY_ENTER]
            if pyola.input.is_key_pressed(key)
        }
        print(self.text)

class ChatRoom:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

