from app_service import AppService
from nest_py.common import controller


@controller
class AppController:
    
    def __init__(self, app_service: AppService) -> None:
        self.app_service = app_service

    def get_hello(self) -> str:
        return self.app_service.get_hello()
