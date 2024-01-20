from .entity import Entity
from flappy_animal.core.commons import random
from flappy_animal.core.utils import List, Union, Tuple
from flappy_animal.core.wrapper import PyGameWrapper, pygame
from flappy_animal.core.display import Window
class Pipe(Entity):
    def __init__(self, speed: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.vel_x: Union[int, float] = -3 * speed

    def draw(self) -> None:
        self.x += self.vel_x
        super().draw()


class Pipes(Entity):
    upper: List[Pipe]
    lower: List[Pipe]

    def __init__(self, window: Window, image: str, speed: int) -> None:
        super().__init__(window)
        self.window: Window = window
        self.pipe_gap: int = 160
        self.top: int = 0
        self.speed: int = speed
        self.bottom: int = self.window.viewport_height
        self.upper: List = []
        self.lower: List = []
        self.image: pygame.Surface = PyGameWrapper.image_load("flappy_animal/assets/sprites/" + image)
        self.spawn_initial_pipes()

    def tick(self) -> None:
        if self.can_spawn_pipes():
            self.spawn_new_pipes()
        self.remove_old_pipes()

        for up_pipe, low_pipe in zip(self.upper, self.lower):
            up_pipe.tick()
            low_pipe.tick()

    def stop(self) -> None:
        for pipe in self.upper + self.lower:
            pipe.vel_x = 0

    def can_spawn_pipes(self) -> bool:
        last = self.upper[-1]
        if not last:
            return True

        return self.window.width - (last.x + last.w) > last.w * 2.5

    def spawn_new_pipes(self) -> None:
        upper, lower = self.make_random_pipes()
        self.upper.append(upper)
        self.lower.append(lower)

    def remove_old_pipes(self) -> None:
        for pipe in self.upper:
            if pipe.x < -pipe.w:
                self.upper.remove(pipe)

        for pipe in self.lower:
            if pipe.x < -pipe.w:
                self.lower.remove(pipe)

    def spawn_initial_pipes(self) -> None:
        upper_1, lower_1 = self.make_random_pipes()
        upper_1.x = self.window.width + upper_1.w * 3
        lower_1.x = self.window.width + upper_1.w * 3
        self.upper.append(upper_1)
        self.lower.append(lower_1)

        upper_2, lower_2 = self.make_random_pipes()
        upper_2.x = upper_1.x + upper_1.w * 3.5
        lower_2.x = upper_1.x + upper_1.w * 3.5
        self.upper.append(upper_2)
        self.lower.append(lower_2)

    def make_random_pipes(self) -> Tuple[Pipe, Pipe]:
        base_y = self.window.viewport_height * 0.79

        gap_y = random.randrange(0, int(base_y * 0.6 - self.pipe_gap - ((self.speed/10) * self.pipe_gap)))
        gap_y += int(base_y * 0.2)
        pipe_height = self.image.get_height()
        pipe_x = (self.window.width + 10)

        upper_pipe = Pipe(
            speed=self.speed,
            window=self.window,
            image=PyGameWrapper.transform_flip(self.image.convert_alpha(), False, True),
            x=pipe_x,
            y=gap_y - pipe_height
        )

        lower_pipe = Pipe(
            speed=self.speed,
            window=self.window,
            image=self.image,
            x=pipe_x,
            y=gap_y + self.pipe_gap,
        )

        return upper_pipe, lower_pipe
