from .entity import Entity
from flappy_animal.core.display import Window
class Floor(Entity):
    def __init__(self, window: Window) -> None:
        super().__init__(window, None, 0, window.viewport_height)
        self.vel_x = 4
        self.x_extra = self.w - window.width

    def stop(self) -> None:
        self.vel_x = 0

    def draw(self) -> None:
        self.x = -((-self.x + self.vel_x) % self.x_extra)
        super().draw()