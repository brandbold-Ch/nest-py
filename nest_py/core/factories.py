from typing import Any
from fastapi import FastAPI
import uvicorn


class ArchonFactory:
    
    def __init__(self, app: Any) -> None:
        self.app = FastAPI()

    def listen(self, host: str = "localhost", port: int = 3000) -> None:
        uvicorn.run(self.app, host=host, port=port)
