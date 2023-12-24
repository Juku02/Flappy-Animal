from flappy_animal.core.wrapper import PyGameWrapper

class Clock:
    def __init__(self) -> None:
        self.clock = PyGameWrapper.clock_init()
        
    def tick(self,fps_frame):
        self.clock.tick(fps_frame)