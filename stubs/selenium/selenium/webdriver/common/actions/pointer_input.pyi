from typing import Any

from .input_device import InputDevice as InputDevice
from .interaction import POINTER as POINTER, POINTER_KINDS as POINTER_KINDS

class PointerInput(InputDevice):
    DEFAULT_MOVE_DURATION: int
    type: Any
    kind: Any
    name: Any
    def __init__(self, kind, name) -> None: ...
    def create_pointer_move(
        self,
        duration=...,
        x: Any | None = ...,
        y: Any | None = ...,
        origin: Any | None = ...,
    ) -> None: ...
    def create_pointer_down(self, button) -> None: ...
    def create_pointer_up(self, button) -> None: ...
    def create_pointer_cancel(self) -> None: ...
    def create_pause(self, pause_duration) -> None: ...  # type: ignore
    def encode(self): ...
