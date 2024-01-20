from flappy_animal.core.wrapper import PyGameWrapper, pygame

class Clock:
    def __init__(self) -> None:
        self.clock: pygame.time.Clock = PyGameWrapper.clock_init()
        
    def tick(self, fps_frame: int) -> None:
        self.clock.tick(fps_frame)
