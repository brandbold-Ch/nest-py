from app_module import AppModule
from nest_py.core.factories import ArchonFactory


def bootstrap() -> None:
    app = ArchonFactory(AppModule)
    app.listen("0.0.0.0", 5000)


bootstrap()
