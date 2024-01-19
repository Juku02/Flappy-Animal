from .entity import Entity
from flappy_animal.core.display import Window
from flappy_animal.core.wrapper import PyGameWrapper
class Floor(Entity):
    def __init__(self, window: Window, speed) -> None:
        self.image = PyGameWrapper.image_load("flappy_animal/assets/sprites/base.png")
        super().__init__(window, self.image, 0, window.viewport_height*0.88)
        self.vel_x = 4 * speed
        self.x_extra = self.w - window.width

    def stop(self) -> None:
        self.vel_x = 0

    def draw(self) -> None:
        self.x = -((-self.x + self.vel_x) % self.x_extra)
        super().draw()
