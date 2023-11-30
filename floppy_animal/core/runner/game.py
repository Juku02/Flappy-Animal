from floppy_animal.core.display import Window
from floppy_animal.core.wrapper import PyGameWrapper
from .clock import Clock

class Runner:
    def __init__(self) -> None:
        self.runnig: bool = False
        self.clock: Clock = None
        self.window: Window = None
    
    def start(self) -> None:
        self.window = Window(640, 480)
        self.clock = Clock()
        self.runnig = True
        
        while self.runnig:
            self.running = PyGameWrapper.event_handler()
            self.window.fill((138,43,226))
            self.window.flip()
            self.clock.tick(45)
            
    def stop() -> None:
        PyGameWrapper.close()