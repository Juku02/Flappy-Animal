
from .basic import BasicScene
from flappy_animal.core.utils import Event_value
from flappy_animal.core.config import Parser
from flappy_animal.core.elements import Player, Score, Player_mode, Pipes, Floor
from flappy_animal.core.wrapper import PyGameWrapper
class GameScene(BasicScene):
    def __init__(self, window, background, config_file, change_scane):
        super().__init__("Game", window)
        self.window = window
        self.background = background
        self.parent_scene = change_scane
        self.config = Parser()
        self.score_table = Parser()
        self.score = Score()
        self.config.read_yaml(config_file)
        initial_x = self.config.getint("player", "start_x")
        initial_y = self.config.getint("player", "start_y")
        speed = self.config.getint("difficulty", "speed")
        self.player = Player(self.config.getint("player", "character_splash"), self.window, (initial_x, initial_y))
        self.floor = Floor(self.window, speed)
        self.pipes = Pipes(self.window, "pipe.png", speed)
        self.score.reset()
        self.player.set_mode(Player_mode.NORMAL)
        self.gameOn = 1

    def back_to(self):
        self.change_screen = self.parent_scene
        self.create_event(Event_value.CHANGE_SCENE.value, self.__dict__)
        self.post_event()
        self.change_screen.draw()

    def gameOver(self):

        self.add_textbox("Score",
                         "Wynik: " + str(self.score.score),
                         True,
                         (0, 0, 0),
                         (self.window.width/2 - 130, 220),
                         'pixelfy',
                         60)

        self.add_button("back_to_menu", (self.window.width/2 - 135, 320), "wstecz.png", self.back_to)

    def draw(self):
        self.add_background(self.background)
        if self.player.collided(self.pipes, self.floor):
            self.gameOn = 0
            self.clear()
            self.gameOver()

        for i, pipe in enumerate(self.pipes.upper):
            if self.player.crossed(pipe):
                self.score.add()

        self.floor.tick()
        self.pipes.tick()
        self.player.tick()

    def update(self, **kwargs):
        self.window.update()
        if self.gameOn:
            self.draw()
            super().update(self.window)
        else:
            super().update(self.window)