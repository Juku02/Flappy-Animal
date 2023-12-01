from floppy_animal.core.wrapper import PyGameWrapper
from floppy_animal.core.utils import Even_type

class Handler:
    def quit_event(self) -> bool:
        events = PyGameWrapper.event_get()
        for event in events:
            if event.type == Even_type.QUIT.value[0]:
                return True

        return False