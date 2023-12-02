
class Scene:
    def __init__(self, name) -> None:
        self.name = name
        
    @staticmethod
    def scene_template(window):
        window.set_background(image="floppy_animal/image/background1.png")
        window.flip()
        window.set_background(image="floppy_animal/image/background2.png")
        window.flip()
    
    def init_scene(self,window) -> None:
        if(self.name == 'welcome'):
            Scene.scene_template(window)