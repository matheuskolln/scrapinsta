from typing import Any

from selenium.webdriver.common import service as service

class Service(service.Service):
    service_args: Any
    def __init__(
        self,
        executable_path,
        port: int = ...,
        host: Any | None = ...,
        log_level: Any | None = ...,
        log_file: Any | None = ...,
    ) -> None: ...
    def command_line_args(self): ...
