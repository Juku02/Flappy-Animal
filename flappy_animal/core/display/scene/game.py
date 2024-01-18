from .basic import BasicScene
from flappy_animal.core.utils import Event_value
from flappy_animal.core.config import Parser
from flappy_animal.core.wrapper import pygame
from flappy_animal.core.elements import Player, Score, Player_mode, Pipes, Floor
class GameScene(BasicScene):
    def __init__(self, window, background, config_file, change_scane):
        super().__init__("Game", window)
        self.window = window
        self.background = background
        self.parent_scene = change_scane
        self.config_file = config_file
        self.config = Parser()
        self.score = Score()
        self.config.read_yaml('options.yaml')
        initial_x = self.config.getint("player", "start_x")
        initial_y = self.config.getint("player", "start_y")
        self.player = Player(self.config.getint("player", "character_splash"), self.window, (initial_x, initial_y))
        self.floor = Floor(self.window)
        self.pipes = Pipes(self.window, "pipe.png")
        self.score.reset()
        self.player.set_mode(Player_mode.NORMAL)
        self.endGame = 0

    def Game_Over(self):
        self.add_button("back", (270, 440), "wstecz.png", self.back_to)

    def Playing(self):

        if self.player.collided(self.pipes, self.floor):
            self.endGame = 1

        for i, pipe in enumerate(self.pipes.upper):
            if self.player.crossed(pipe):
                self.score.add()

        self.floor.tick()
        self.pipes.tick()
        self.player.tick()



    def back_to(self):
        self.change_screen = self.parent_scene
        self.create_event(Event_value.CHANGE_SCENE.value, self.__dict__)
        self.post_event()
        self.change_screen.draw()

    def draw(self):
        if not self.endGame:
            self.add_background(self.background)
            self.Playing()
        else:
            self.add_background(self.background)
            self.Game_Over()


    def update(self, **kwargs):
        self.draw()
        super().update(self.window)