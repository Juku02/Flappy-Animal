from flappy_animal.core.utils import Even_value
from flappy_animal.core.game_events import Handler
from flappy_animal.core.wrapper import PyGameWrapper
class Button(object):
    def __init__(self, name, location, image, window, function):
        self.name = name
        self.window = window
        self.funtion = function
        self.button_x = location[0]
        self.button_y = location[1]
        self.image_name = image
        self.button_width = None
        self.button_height = None
        self.end_x = None
        self.end_y = None
        self.clicked = False

    def draw(self):
        img = PyGameWrapper.image_load("flappy_animal/assets/buttons/" + self.image_name)
        self.end_x = img.get_width() + self.button_x
        self.end_y = img.get_height() + self.button_y
        self.window.blit(img, (self.button_x, self.button_y))

    def click(self, window):
        # print(window.handler.event_handler())
        # clicked = window.handler.process_events()
        # print(window.handler.process_events())
        # if clicked == Even_value.MOUSE_CLICK.value:
        print("Pressed mouse button")
        #     func = self.funtion
        #     func()
        # else:
        #     self.clicked = True
