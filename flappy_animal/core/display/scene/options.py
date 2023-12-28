from flappy_animal.core.config import Parser
from .basic import BasicScene
from flappy_animal.core.utils import Event_value
class OptionScene(BasicScene):
    def __init__(self, window, background,config_file, change_scane):
        super().__init__("Options", window)
        self.window = window
        self.background = background
        self.config_file = config_file
        self.config = Parser()
        self.parent_scene = change_scane
        self.character_index = 1
        self.difficulty_index = 1

    def character_choose(self, index):
        self.character_index += index
        if 0 < self.character_index <= 3:
            for box in self.text_boxes:
                if box.name == 'Character_index':
                    self.clear()
                    box.update(text=str(self.character_index))
        else:
            self.character_index -= index

    def difficulty_choose(self, index):
        self.difficulty_index += index
        if 0 < self.difficulty_index <= 5:
            for box in self.text_boxes:
                if box.name == 'Difficulty_index':
                    self.clear()
                    box.update(text=str(self.difficulty_index))
        else:
            self.difficulty_index -= index

    def back_to(self):
        self.change_screen = self.parent_scene
        self.create_event(Event_value.CHANGE_SCENE.value, self.__dict__)
        self.post_event()
        self.change_screen.draw()

    def draw(self):
        self.add_background(self.background)
        self.add_textbox("Character",
                         "Choose Character",
                         True,
                         (0, 0, 0),
                         (self.window.width/2 - 250, 100),
                         'pixelfy',
                         60)
        self.add_button("Left_char_button",
                        (self.window.width/2 - 300, 160),
                        "arrow_left.png",
                        self.character_choose,
                        (-1))
        self.add_textbox("Character_index",
                         str(self.character_index),
                         True,
                         (0, 0, 0),
                         (self.window.width/2 - 10, 170),
                         'pixelfy',
                         60)
        self.add_button("Right_char_button",
                        (self.window.width / 2 + 100, 160),
                        "arrow_right.png",
                        self.character_choose,
                        1)
        self.add_textbox("Difficulty",
                         "Choose Difficulty",
                         True,
                         (0, 0, 0),
                         (self.window.width/2 - 250, 250),
                         'pixelfy',
                         60)
        self.add_button("Left_dif_button",
                        (self.window.width / 2 - 300, 310),
                        "arrow_left.png",
                        self.difficulty_choose,
                        (-1))
        self.add_textbox("Difficulty_index",
                         str(self.difficulty_index),
                         True,
                         (0, 0, 0),
                         (self.window.width / 2 - 10, 310),
                         'pixelfy',
                         60)
        self.add_button("Right_dif_button",
                        (self.window.width / 2 + 100, 310),
                        "arrow_right.png",
                        self.difficulty_choose,
                        1)
        self.add_button("Back",
                        (270, 440),
                        "wstecz.png",
                        self.back_to)

    def update(self, **kwargs):
        self.window.update()
        super().update(self.window)