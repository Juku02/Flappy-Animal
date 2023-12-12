from floppy_animal.core.display import Window, Scene
from floppy_animal.core.wrapper import PyGameWrapper
from floppy_animal.core.utils import Even_type
from floppy_animal.core.game_events import Handler
from .clock import Clock

class Runner:
    def __init__(self) -> None:
        self.window: Window = Window(1900, 1080)
        self.clock: Clock = Clock()
        self.handler: Handler = Handler()
        self.running:bool = None
        self.welcome_screen = None
        
    def initiation(self):
        self.running = True
        self.welcome_screen = Scene("welcome", self.window)
        self.welcome_screen.run_scene()
        
        
    def start(self) -> None:
        self.initiation()
        while self.running:
            if self.handler.quit_event():
                self.running = False
            
               
            
            self.clock.tick(60)
            self.window.update()
        
    def stop(self) -> None:
        PyGameWrapper.close()