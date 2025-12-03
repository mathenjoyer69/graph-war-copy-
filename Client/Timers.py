import pyola
import time

class Timer:
    def __init__(self, duration, x, y, width, height, color=(0, 1, 0)):
        self.duration = duration
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.start_time = None
        self.running = False
        self.rect = pyola.shapes.Rectangle(x, y, width, height, color=color)

    def draw(self):
        self.rect.draw()