from .basic import BasicScene
from flappy_animal.core.wrapper import PyGameWrapper
class GameScene(BasicScene):
    def __init__(self, window, background):
        super().__init__("Game", window)
        self.window = window
        self.background = background

    def Playing(self):
        pass

    def Game_Over(self):
        pass

    @staticmethod
    def exit_game():
        PyGameWrapper.update()
        PyGameWrapper().close()

    def create(self):
        self.add_background(self.background)
        self.add_textbox("Floppy Animal", True, (0, 0, 0), (80, 100), 'pixelfy', 96)
        self.add_button("start", (270, 200), "start.png")
        self.add_button("options", (270, 320), "opcje.png")
        self.add_button("exit", (270, 440), "wyjscie.png", self.exit_game)

    def update(self, **kwargs):
        super().update(self.window)