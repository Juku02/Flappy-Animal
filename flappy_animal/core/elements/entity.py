from flappy_animal.core.utils import get_hit_mask, pixel_collision, Union
from flappy_animal.core.display import Window
from flappy_animal.core.wrapper import pygame

class Entity:
    def __init__(
        self,
        window: Window,
        image: pygame.Surface = None,
        x: Union[int, float] = 0,
        y: Union[int, float] = 0,
        w: Union[int, float] = None,
        h: Union[int, float] = None,
        **kwargs,
    ) -> None:
        self.window: Window = window
        self.x: Union[int, float] = x
        self.y: Union[int, float] = y
        if w or h:
            self.w: Union[int, float] = w or window.ratio * h
            self.h: Union[int, float] = h or w / window.ratio
            self.image:  pygame.Surface = pygame.transform.scale(image, (self.w, self.h))
        else:
            self.image:  pygame.Surface = image
            self.w = image.get_width() if image else 0
            self.h = image.get_height() if image else 0

        self.hit_mask = get_hit_mask(image) if image else None
        self.__dict__.update(kwargs)

    def update_image(
        self, image: pygame.Surface, w: int = None, h: int = None
    ) -> None:
        self.image = image
        self.hit_mask = get_hit_mask(image)
        self.w = w or (image.get_width() if image else 0)
        self.h = h or (image.get_height() if image else 0)

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def cy(self) -> float:
        return self.y + self.h / 2

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def collide(self, other) -> bool:
        if not self.hit_mask or not other.hit_mask:
            return self.rect.colliderect(other.rect)
        return pixel_collision(
            self.rect, other.rect, self.hit_mask, other.hit_mask
        )

    def tick(self) -> None:
        self.draw()

    def draw(self) -> None:
        if self.image:
            self.window.blit(self.image, self.rect)
