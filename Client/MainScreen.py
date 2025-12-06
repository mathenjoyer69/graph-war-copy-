import time
import pyola
import Client.Helpers

settings = Client.Helpers.load_json("C:\\Users\\ariel\\PycharmProjects\\graph-war\\Client\\settings.json")


class MainScreen:
    def __init__(self, win):
        self.screen_width = settings["width"]
        self.screen_height = settings["height"]

        self.join_local_button = Client.Helpers.Button(150, self.screen_height - 150, 200, 50, "join local")
        self.join_global_button = Client.Helpers.Button(400, self.screen_height - 150, 200, 50, "join global")

    def update(self):
        if self.join_local_button.is_clicked():
            print("join local")

    def draw(self):
        self.join_local_button.draw()
        self.join_global_button.draw()


def run_client():
    win = pyola.window.Window(settings["width"], settings["height"], "Graph War")

    current_scene = MainScreen(win)

    while win.running:
        pyola.renderer.clear((0.2, 0.2, 0.2))
        current_scene.update()
        current_scene.draw()

        win.update()
        time.sleep(1 / 60)
    win.close()


if __name__ == "__main__":
    run_client()
