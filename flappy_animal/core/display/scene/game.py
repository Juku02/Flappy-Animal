
from .basic import BasicScene, Window
from flappy_animal.core.utils import Event_value, Any
from flappy_animal.core.config import Parser
from flappy_animal.core.elements import Player, Score, Player_mode, Pipes, Floor
class GameScene(BasicScene):
    def __init__(self, window: Window, background: str, config_file: str, score_file: str, change_scane: Any):
        super().__init__("Game", window)
        self.window: Window = window
        self.background: str = background
        self.parent_scene: Any = change_scane
        self.config: Parser = Parser()
        self.score_table: Parser = Parser()
        self.score: Score = Score()
        self.config.read_yaml(config_file)
        self.score_table.read_yaml(score_file)
        self.config_file: str = config_file
        self.score_file: str = score_file
        initial_x = self.config.getint("player", "start_x")
        initial_y = self.config.getint("player", "start_y")
        speed = self.config.getint("difficulty", "speed")
        self.player: Player = Player(self.config.getint("player", "character_splash"), self.window, (initial_x, initial_y))
        self.floor: Floor = Floor(self.window, speed)
        self.pipes: Pipes = Pipes(self.window, "pipe.png", speed)
        self.score.reset()
        self.player.set_mode(Player_mode.NORMAL)
        self.gameOn: bool = True

    def back_to(self) -> None:
        self.change_screen = self.parent_scene
        self.create_event(Event_value.CHANGE_SCENE.value, self.__dict__)
        self.post_event()
        self.change_screen.draw()

    def gameOver(self) -> None:
        self.add_textbox("Score",
                         "Wynik: " + str(self.score.score),
                         True,
                         (0, 0, 0),
                         (self.window.width/2 - 130, 50),
                         'pixelfy',
                         60)
        self.add_textbox("Score",
                         "Tablica wynikow",
                         True,
                         (0, 0, 0),
                         (self.window.width / 2 - 270, 100),
                         'pixelfy',
                         60)
        next_score = 150
        score_table = []
        for place in self.score_table.options("score_table"):
            score_table.append((int(place), int(self.score_table.get("score_table", place))))

        if self.score.score not in score_table:
            score_table.append((len(self.score_table.options("score_table")), self.score.score))

        score_table = sorted(score_table, key=lambda x: x[1], reverse=True)
        score_table = [(i + 1, score) for i, (place, score) in enumerate(score_table)]

        for place in score_table:
            self.add_textbox("Score",
                        str(place[0]) + ": " + str(place[1]),
                        True,
                        (0, 0, 0),
                        (self.window.width / 2 - 55, next_score),
                        'pixelfy',
                        52)
            next_score+=50
            self.score_table.set("score_table", str(place[0]), str(place[1]))
            self.score_table.write_yaml(self.score_file)

        self.add_button("back_to_menu", (self.window.width/2 - 135, 500), "wstecz.png", self.back_to)

    def draw(self) -> None:
        self.add_background(self.background)
        if self.player.collided(self.pipes, self.floor):
            self.gameOn = False
            self.clear()
            self.gameOver()

        for i, pipe in enumerate(self.pipes.upper):
            if self.player.crossed(pipe):
                self.score.add()

        self.floor.tick()
        self.pipes.tick()
        self.player.tick()

    def update(self, **kwargs) -> None:
        self.window.update()
        if self.gameOn:
            self.draw()
            super().update(self.window)
        else:
            super().update(self.window)
