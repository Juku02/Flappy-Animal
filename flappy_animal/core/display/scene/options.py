from flappy_animal.core.config import Parser
from .basic import BasicScene
from flappy_animal.core.wrapper import PyGameWrapper
class OptionScene(BasicScene):
    def __init__(self, window, background,config_file):
        super().__init__("Options", window)
        self.window = window
        self.background = background
        self.config_file = config_file
        self.config = Parser

    def CharacterChoose(self):
        # if self.config.has_section():
            pass

    def Difficulty(self):
        pass

    @staticmethod
    def back_to():
        PyGameWrapper.update()



    def draw(self):
        self.add_background(self.background)
        self.add_textbox("title","Floppy Animal", True, (0, 0, 0), (80, 100), 'pixelfy', 96)
        self.add_textbox("title","Floppy Animal", True, (0, 0, 0), (80, 100), 'pixelfy', 96)
        self.add_textbox("title","Floppy Animal", True, (0, 0, 0), (80, 100), 'pixelfy', 96)
        self.add_button("Back", (270, 440), "wyjscie.png", self.back_to)

    def update(self, **kwargs):
        super().update(self.window)