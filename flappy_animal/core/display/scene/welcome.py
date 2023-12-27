from flappy_animal.core.utils import Event_value
from .basic import BasicScene
from .options import OptionScene
from flappy_animal.core.wrapper import PyGameWrapper
class WelcomeScene(BasicScene):
    def __init__(self, window, background):
        super().__init__("Welcome", window)
        self.window = window
        self.background = background

    def start_game(self):
        pass

    def to_options(self):
        self.child_screen = OptionScene(self.window, self.background, "options.yaml")
        self.create_event(Event_value.CHANGE_SCENE.value, self.__dict__)
        self.post_event()
        self.child_screen.draw()
        # print("Go to the options")

        # self.child_scene.append()

    @staticmethod
    def exit_game():
        PyGameWrapper.update()
        PyGameWrapper().close()

    def draw(self):
        self.add_background(self.background)
        self.add_textbox("title", "Flappy Animal", True, (0, 0, 0), (self.window.width/2 - 300, 100), 'pixelfy', 96)
        self.add_button("start", (self.window.width/2 - 135, 200), "start.png", self.start_game)
        self.add_button("options", (self.window.width/2 - 135, 320), "opcje.png", self.to_options)
        self.add_button("exit", (self.window.width/2 - 135, 440), "wyjscie.png", self.exit_game)

    def update(self, **kwargs):
        self.window.update()
        super().update(self.window)