from .basic import BasicScene

class WelcomeScene(BasicScene):
    def __init__(self, window, background):
        super().__init__("Welcome", window)
        self.window = window
        self.background = background

    def start_game(self):
        pass

    def to_options(self):
        pass

    def exit_game(self):
        print("dupa")

    def create(self):
        self.add_background(self.background)
        self.add_textbox("Floppy Animal", True, (0, 0, 0), (80, 100), 'pixelfy', 96)
        self.add_button("start", (270, 200), "start.png")
        self.add_button("options", (270, 320), "opcje.png")
        self.add_button("exit", (270, 440), "wyjscie.png", self.exit_game)

    def update(self):
        super().update(self.window)