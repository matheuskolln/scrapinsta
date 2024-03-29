from typing import Any

from selenium.webdriver.common import service as service

class Service(service.Service):
    service_args: Any
    def __init__(
        self,
        executable_path,
        port: int = ...,
        service_args: Any | None = ...,
        log_path: str = ...,
        env: Any | None = ...,
    ) -> None: ...
    def command_line_args(self): ...
    def send_remote_shutdown_command(self) -> None: ...
