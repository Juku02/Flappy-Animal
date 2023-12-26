from flappy_animal.core.wrapper import PyGameWrapper
class Button(object):
    def __init__(self, name, location, image, window, function):
        self.name = name
        self.window = window
        self.funtion = function
        self.location = location
        self.image_name = image
        self.button_width = None
        self.button_height = None
        self.end_x = None
        self.end_y = None
        self.clicked = False

    def draw(self):
        img = PyGameWrapper.image_load("flappy_animal/assets/buttons/" + self.image_name)
        self.end_x = img.get_width() + self.location[0]
        self.end_y = img.get_height() + self.location[1]
        self.window.blit(img, self.location)

    def click(self):
        if self.funtion is not None:
            self.funtion()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
