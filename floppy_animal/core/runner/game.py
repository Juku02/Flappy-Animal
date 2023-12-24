from floppy_animal.core.display import Window, WelcomeScene
from floppy_animal.core.wrapper import PyGameWrapper
from floppy_animal.core.game_events import Handler
from floppy_animal.core.utils import Even_value
from .clock import Clock


class Runner:
    def __init__(self) -> None:
        self.window: Window = Window(800, 600, Handler())
        self.clock: Clock = Clock()
        self.running: bool = False
        self.welcome_screen = None

    def initiation(self):
        self.running = True
        self.window.caption("Floppy Animal")
        self.welcome_screen = WelcomeScene(self.window, "welcome.png")
        self.welcome_screen.create()

    def start(self) -> None:
        self.initiation()
        while self.running:
            self.window.handler.event_handler()
            if self.window.handler.process_events() == Even_value.QUIT.value:
                self.running = False

            self.clock.tick(60)
            self.window.update()
            self.welcome_screen.update()

    @staticmethod
    def stop() -> None:
        PyGameWrapper.close()

