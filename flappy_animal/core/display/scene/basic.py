from flappy_animal.core.wrapper import PyGameWrapper
from flappy_animal.core.controls import Button, TextBox
from flappy_animal.core.utils import Event_value
class BasicScene:
    def __init__(self, name, window) -> None:
        self.name = name
        self.window = window
        self.font = None
        self.background = None
        self.text_boxes = []
        self.buttons = []
        self.change_screen = None
        self.event = None

    def add_background(self, background_image):
        self.window.set_background(image=background_image)

    def add_textbox(self, name, text, antialiasing, color, location, font, size):
        text_box = TextBox( name, text, location, antialiasing, color, font, size)
        self.text_boxes.append(text_box)

    def add_button(self, name, location, image, func=None):
        button = (Button(name, location, image, self.window, func))
        self.buttons.append(button)

    def create_event(self, type, data):
        self.event = PyGameWrapper.make_event(type, data)

    def post_event(self):
        PyGameWrapper.post_event(self.event)

    def clear(self):
        self.window.set_background(image=self.background)

    def update(self, window):
        PyGameWrapper.update()
        for box in self.text_boxes:
            box.draw()
            self.window.blit(box.surface, box.location)
        for button in self.buttons:
            button.draw()