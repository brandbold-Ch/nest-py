from typing import Any, Callable, Optional, List
from fastapi.types import DecoratedCallable
from nest_py.utils.artifacts import tree, Controller, class_name, Module, Injectable
import inspect


def module(
    imports: Optional[List[Any]] = None,
    controllers: Optional[List[Any]] = None,
    providers: Optional[List[Any]] = None,
    exports: Optional[List[Any]] = None
) -> Callable[[DecoratedCallable], DecoratedCallable]:
    def wrapper(cls: Any) -> Any:
        mod = Module(
            imports=imports, 
            controllers=controllers, 
            providers=providers, 
            exports=exports
        )
        tree.add_module(class_name(cls), mod)        
        
        return cls
    return wrapper


def injectable(cls) -> Any:
    injt = Injectable(clazz=cls)
    tree.add_injectable(class_name(cls), injt)
    return cls


def controller(
    prefix: str = "/"
) -> Callable[[DecoratedCallable], DecoratedCallable]:
    def decorator(cls: Any) -> Any:
        funcs = inspect.getmembers(cls, inspect.isfunction)
        ctrl = Controller(path=prefix, clazz=cls)
        
        for name, func in funcs:
            if hasattr(func, "_route"):
                ctrl.add_route(name, func)
        tree.add_controller(class_name(cls), ctrl)                
        
        return cls
    return decorator
