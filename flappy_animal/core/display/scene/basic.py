from flappy_animal.core.wrapper import PyGameWrapper
from flappy_animal.core.controls import Button, TextBox
from flappy_animal.core.utils import List, Tuple, Any
from flappy_animal.core.wrapper import pygame
from ..window import Window

class BasicScene:
    def __init__(self, name: str, window: Window) -> None:
        self.name: str = name
        self.window: Window = window
        self.font: pygame.font.Font = None
        self.background: str = None
        self.text_boxes: List = []
        self.buttons: List = []
        self.change_screen = None
        self.event: pygame.event.Event = None

    def add_background(self, background_image: str = None) -> None:
        self.window.set_background(image=background_image)

    def add_textbox(self, name: str, text: str, antialiasing: bool, color: Tuple, location: Tuple, font: str, size: bytes) -> None:
        text_box = TextBox(name, text, location, antialiasing, color, font, size)
        self.text_boxes.append(text_box)

    def add_button(self, name: str, location: Tuple, image: str, func=None, func_args=None) -> None:
        button = (Button(name, location, image, self.window, func, func_args))
        self.buttons.append(button)

    def create_event(self, type: pygame.event.EventType, data: Any) -> None:
        self.event = PyGameWrapper.make_event(type, data)

    def post_event(self) -> None:
        PyGameWrapper.post_event(self.event)

    def clear(self) -> None:
        self.window.set_background(image=self.background)

    def update(self, window: Window) -> None:
        PyGameWrapper.update()
        if self.text_boxes is not None:
            for box in self.text_boxes:
                box.draw()
                self.window.blit(box.surface, box.location)
        if self.buttons is not None:
            for button in self.buttons:
                button.draw()
                