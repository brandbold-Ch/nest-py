from nest_py.common import module


@module(
    controllers=["AppController"],
    providers=["AppService"],
)
class AppModule:
    pass
