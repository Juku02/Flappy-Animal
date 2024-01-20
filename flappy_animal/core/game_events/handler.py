from flappy_animal.core.wrapper import PyGameWrapper, pygame
from flappy_animal.core.utils import Event_value, Event_type, Tuple, List, Union, Dict, Any

class Handler:
    event_queue: List = []

    def add_event(self, event: Union[Tuple[Event_type, Dict], Event_type]) -> None:
        self.event_queue.append(event)

    def event_handler(self) -> None:
        for event in PyGameWrapper.event_get():
            if event.type == Event_value.QUIT.value[0]:
                self.add_event(Event_type.QUIT)
            elif event.type == Event_value.MOUSE_CLICK.value[0]:
                self.add_event((Event_type.MOUSE_CLICK, event.dict['pos']))
            elif event.type == Event_value.WINDOW_RESIZE.value:
                self.add_event((Event_type.WINDOW_RESIZE, event.dict['size']))
            elif event.type == Event_value.CHANGE_SCENE.value:
                self.add_event((Event_type.CHANGE_SCENE, event.dict))

        return None

    def process_events(self) -> Any:
        while self.event_queue:
            event = self.event_queue.pop()
            if event == Event_type.QUIT:
                return Event_value.QUIT.value
            elif event[0] == Event_type.MOUSE_CLICK:
                return Event_value.MOUSE_CLICK.value, event[1]
            elif event[0] == Event_type.WINDOW_RESIZE:
                return Event_value.WINDOW_RESIZE.value, event[1]
            elif event[0] == Event_type.CHANGE_SCENE:
                return Event_value.CHANGE_SCENE.value, event[1]
        return None
