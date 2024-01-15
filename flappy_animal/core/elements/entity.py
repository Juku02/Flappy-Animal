from flappy_animal.core.utils import get_hit_mask, pixel_collision
from flappy_animal.core.display import Window
from flappy_animal.core.wrapper import pygame

class Entity:
    def __init__(
        self,
        window: Window,
        image = None,
        x=0,
        y=0,
        w: int = None,
        h: int = None,
        **kwargs,
    ) -> None:
        self.window = window
        self.x = x
        self.y = y
        if w or h:
            self.w = w or window.ratio * h
            self.h = h or w / window.ratio
            self.image = pygame.transform.scale(image, (self.w, self.h))
        else:
            self.image = image
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