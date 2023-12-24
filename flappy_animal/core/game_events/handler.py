from flappy_animal.core.wrapper import PyGameWrapper
from flappy_animal.core.utils import Even_value, Event_type, Tuple

class Handler:
    event_queue = []

    def add_event(self, event):
        self.event_queue.append(event)

    def event_handler(self):
        for event in PyGameWrapper.event_get():
            if event.type == Even_value.QUIT.value[0]:
                self.add_event(Event_type.QUIT)
            elif event.type == Even_value.MOUSE_CLICK.value[0]:
                self.add_event((Event_type.MOUSE_CLICK, (event.dict.get('pos'))))
        return None

    def process_events(self):
        while self.event_queue:
            event = self.event_queue.pop()
            if event == Event_type.QUIT:
                return Even_value.QUIT.value
            elif event[0] == Event_type.MOUSE_CLICK:
                return Even_value.MOUSE_CLICK.value, event[1]
        return None
