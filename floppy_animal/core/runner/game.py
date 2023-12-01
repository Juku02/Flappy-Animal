from floppy_animal.core.display import Window
from floppy_animal.core.wrapper import PyGameWrapper
from floppy_animal.core.utils import Even_type
from floppy_animal.core.game_events import Handler
from .clock import Clock

class Runner:
    def __init__(self) -> None:
        self.window: Window = Window(1900, 1080)
        self.clock: Clock = Clock()
        self.handler: Handler = Handler()
        self.running:bool = True
        
    def start(self) -> None:
        while self.running:
            if self.handler.quit_event():
                self.running = False
                
            self.window.set_background(image="floppy_animal/image/background.jpg")
            self.window.flip()
            self.clock.tick(60)
        
    def stop(self) -> None:
        PyGameWrapper.close()