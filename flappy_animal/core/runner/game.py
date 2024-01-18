from flappy_animal.core.display import Window, WelcomeScene, OptionScene
from flappy_animal.core.wrapper import PyGameWrapper
from flappy_animal.core.game_events import Handler
from flappy_animal.core.utils import Event_value
from .clock import Clock


class Runner:
    def __init__(self) -> None:
        self.window: Window = Window(800, 600, Handler())
        self.clock: Clock = Clock()
        self.running: bool = False
        self.welcome_screen = None
        self.actual_screen = None

    def initiation(self):
        self.running = True
        self.window.caption("Floppy Animal")
        self.welcome_screen = WelcomeScene(self.window, "welcome.png")
        self.welcome_screen.draw()

    def start(self) -> None:
        self.initiation()
        self.actual_screen = self.welcome_screen
        while self.running:
            self.window.handler.event_handler()
            event = self.window.handler.process_events()
            if event is not None:
                if event == Event_value.QUIT.value:
                    self.running = False
                elif event[0] == Event_value.MOUSE_CLICK.value:
                    if self.actual_screen.buttons:
                        position = event[1]
                        for button in self.actual_screen.buttons:
                            if button.location[0] <= position[0] <= button.end_x and button.location[1] <= position[1] <= button.end_y:
                                button.click()
                    else:
                        self.actual_screen.player.flap()

                elif event[0] == Event_value.WINDOW_RESIZE.value:
                    size = event[1]
                    self.window.update(win_size=size)
                    self.window.resize(size, self.actual_screen)

                elif event[0] == Event_value.CHANGE_SCENE.value:
                    screen = event[1]
                    self.actual_screen.clear()
                    self.actual_screen = screen['change_screen']
                    self.actual_screen.update()


            self.clock.tick(40)
            self.actual_screen.update()

    @staticmethod
    def stop() -> None:
        PyGameWrapper.close()

