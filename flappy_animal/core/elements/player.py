from flappy_animal.core.utils import Player_mode, clamp, Tuple, Union, Any
from flappy_animal.core.wrapper import PyGameWrapper, pygame
from flappy_animal.core.display import Window
from .entity import Entity
from .pipe import Pipe, Pipes
from .floor import Floor

class Player(Entity):
    def __init__(self, splash: int, window: Window, initial_position: Tuple) -> None:
        self.splash: pygame.Surface = PyGameWrapper.image_load("flappy_animal/assets/sprites/" + str(splash) + ".png")
        x = int(initial_position[0])
        y = int(initial_position[1])
        super().__init__(window=window, image=self.splash, x=x, y=y)
        self.min_y: Union[int, float] = 0
        self.max_y:  Union[int, float] = window.viewport_height - window.height * 0.2
        self.mode: Player_mode = None
        self.img_idx: int = 0
        self.frame: int = 0
        self.crashed: bool = False
        self.crash_entity: Any = None
        self.set_mode(Player_mode.SHM)

    def set_mode(self, mode: Player_mode) -> None:
        self.mode = mode
        if mode == Player_mode.NORMAL:
            self.reset_vals_normal()
        elif mode == Player_mode.SHM:
            self.reset_vals_shm()
        elif mode == Player_mode.CRASH:
            self.reset_vals_crash()

    def reset_vals_normal(self) -> None:
        self.vel_y = -5  # player's velocity along Y axis
        self.max_vel_y = 10  # max vel along Y, max descend speed
        self.min_vel_y = -8  # min vel along Y, max ascend speed
        self.acc_y = 1  # players downward acceleration

        self.rot = 80  # player's current rotation
        self.vel_rot = -3  # player's rotation speed
        self.rot_min = -90  # player's min rotation angle
        self.rot_max = 20  # player's max rotation angle

        self.flap_acc = -9  # players speed on flapping
        self.flapped = False  # True when player flaps

    def reset_vals_shm(self) -> None:
        self.vel_y = 1  # player's velocity along Y axis
        self.max_vel_y = 4  # max vel along Y, max descend speed
        self.min_vel_y = -4  # min vel along Y, max ascend speed
        self.acc_y = 0.5  # players downward acceleration

        self.rot = 0  # player's current rotation
        self.vel_rot = 0  # player's rotation speed
        self.rot_min = 0  # player's min rotation angle
        self.rot_max = 0  # player's max rotation angle

        self.flap_acc = 0  # players speed on flapping
        self.flapped = False  # True when player flaps

    def reset_vals_crash(self) -> None:
        self.acc_y = 2
        self.vel_y = 7
        self.max_vel_y = 15
        self.vel_rot = -8

    def tick_shm(self) -> None:
        if self.vel_y >= self.max_vel_y or self.vel_y <= self.min_vel_y:
            self.acc_y *= -1
        self.vel_y += self.acc_y
        self.y += self.vel_y

    def tick_normal(self) -> None:
        if self.vel_y < self.max_vel_y and not self.flapped:
            self.vel_y += self.acc_y
        if self.flapped:
            self.flapped = False

        self.y = clamp(self.y + self.vel_y, self.min_y, self.max_y)
        self.rotate()

    def tick_crash(self) -> None:
        if self.min_y <= self.y <= self.max_y:
            self.y = clamp(self.y + self.vel_y, self.min_y, self.max_y)
            # rotate only when it's a pipe crash and bird is still falling
            if self.crash_entity != "floor":
                self.rotate()

        # player velocity change
        if self.vel_y < self.max_vel_y:
            self.vel_y += self.acc_y

    def rotate(self) -> None:
        self.rot = clamp(self.rot + self.vel_rot, self.rot_min, self.rot_max)

    def draw(self) -> None:
        if self.mode == Player_mode.SHM:
            self.tick_shm()
        elif self.mode == Player_mode.NORMAL:
            self.tick_normal()
        elif self.mode == Player_mode.CRASH:
            self.tick_crash()

        self.draw_player()

    def draw_player(self) -> None:
        rotated_image = PyGameWrapper.rotate(self.image, self.rot)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        self.window.blit(rotated_image, rotated_rect)

    def flap(self) -> None:
        if self.y > self.min_y:
            self.vel_y = self.flap_acc
            self.flapped = True
            self.rot = 80

    def crossed(self, pipe: Pipe) -> bool:
        return pipe.cx <= self.cx < pipe.cx - pipe.vel_x

    def collided(self, pipes: Pipes, floor: Floor) -> bool:
        if self.collide(floor):
            self.crashed = True
            self.crash_entity = "floor"
            return True

        for pipe in pipes.upper:
            if self.collide(pipe):
                self.crashed = True
                self.crash_entity = "pipe"
                return True
        for pipe in pipes.lower:
            if self.collide(pipe):
                self.crashed = True
                self.crash_entity = "pipe"
                return True

        return False
