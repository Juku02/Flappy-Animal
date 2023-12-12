from floppy_animal.core.wrapper import PyGameWrapper

class Scene:
    def __init__(self, name,window) -> None:
        self.name = name
        self.window = window
        self.font = None
        self.background = "background1.png"
    
    def add_background(self):
        self.window.set_background(image=self.background)

    
    def write_textbox(self,text,antialiasing, color, location):
        text_surf = self.font.render(text, antialiasing, color)
        self.window.blit(text_surf, location)
    
    def run_scene(self) -> None:
        # self.animate_background()
        if self.name == "welcome":
            self.add_background()
            self.font = PyGameWrapper.set_font('pixelfy',82)
            self.write_textbox("Floppy Animal", True, (0, 0, 0), (650,200))
            self.write_textbox("Start", True, (255, 196, 126), (800,600))
            self.write_textbox("Opcje", True, (255, 196, 126), (820,700))
            self.write_textbox("Wyjscie", True,(255, 173, 132), (780,800))