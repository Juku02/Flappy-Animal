from flappy_animal.core.config import Parser
from .basic import BasicScene
# from flappy_animal.core.wrapper import PyGameWrapper
from flappy_animal.core.utils import Event_value
class OptionScene(BasicScene):
    def __init__(self, window, background,config_file, change_scane):
        super().__init__("Options", window)
        self.window = window
        self.background = background
        self.config_file = config_file
        self.config = Parser
        self.parent_scene = change_scane

    def CharacterChoose(self):
        # if self.config.has_section():
            pass

    def Difficulty(self):
        pass

    def back_to(self):
        self.change_screen = self.parent_scene
        self.create_event(Event_value.CHANGE_SCENE.value, self.__dict__)
        self.post_event()
        self.change_screen.draw()

    def draw(self):
        self.add_background(self.background)
        self.add_textbox("Character","Choose Character", True, (0, 0, 0), (self.window.width/2 - 250, 100), 'pixelfy', 60)
        self.add_textbox("Difficulty","Choose Difficulty", True, (0, 0, 0), (self.window.width/2 - 250, 250), 'pixelfy', 60)
        # self.add_textbox("title","Floppy Animal", True, (0, 0, 0), (self.window.width/2 - 300, 400), 'pixelfy', 96)
        self.add_button("Back", (270, 440), "wstecz.png", self.back_to)

    def update(self, **kwargs):
        self.window.update()
        super().update(self.window)