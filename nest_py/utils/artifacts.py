from fastapi.routing import APIRoute
from typing import Optional, Callable, Any, List, Union, Sequence, Dict, Type
from dataclasses import dataclass, field
from starlette.routing import BaseRoute
from starlette.responses import Response, JSONResponse
from fastapi.types import IncEx
from enum import Enum
from fastapi.datastructures import Default
from fastapi.utils import generate_unique_id
from fastapi.params import Depends


class Singlenton:
    _instance: Optional["Singlenton"] = None

    def __new__(cls, *args, **kwargs) -> "Singlenton":
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


@dataclass
class Endpoint:
    path: Optional[str] = None
    methods: Optional[str] = None
    endpoint: Optional[Callable] = None
    controller: Optional[Callable] = field(metadata={"exclude": True}, default=None)
    module: Optional[str] = field(metadata={"exclude": True}, default=None)
    response_model: Any = Default(None)
    status_code: Optional[int] = None
    tags: Optional[List[Union[str, Enum]]] = None
    dependencies: Optional[Sequence[Depends]] = None
    summary: Optional[str] = None
    description: Optional[str] = None,
    response_description: Optional[str] = None
    responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None
    deprecated: Optional[bool] = None
    methods: Optional[List[str]] = None
    operation_id: Optional[str] = None
    response_model_include: Optional[IncEx] = None
    response_model_exclude: Optional[IncEx] = None
    response_model_by_alias: bool = True
    response_model_exclude_unset: bool = False
    response_model_exclude_defaults: bool = False
    response_model_exclude_none: bool = False
    include_in_schema: bool = True
    response_class: Type[Response] = Default(JSONResponse)
    name: Optional[str] = None
    callbacks: Optional[List[BaseRoute]] = None
    openapi_extra: Optional[Dict[str, Any]] = None
    generate_unique_id_function: Callable[[APIRoute], str] = Default(
        generate_unique_id
    )


@dataclass
class Injectable:
    clazz: Any
    depends: Dict[str, Any] = field(default_factory=dict)
    
    def add_depend(self, key, value) -> None:
        self.depends[key] = value


@dataclass
class Controller:
    path: str
    clazz: Any = None
    routes: Dict[str, Callable] = field(default_factory=dict)
    
    def add_route(self, key, value) -> None:
        self.routes[key] = value


@dataclass
class Module:
    imports: Optional[List[Any]]
    controllers: Optional[List[Any]]
    providers: Optional[List[Any]]
    exports: Optional[List[Any]]


class ArchonContainer(Singlenton):
    
    def __new__(cls, *args, **kwargs) -> "ArchonContainer":
        return super().__new__(cls, *args, **kwargs)
    
    def __init__(self) -> None:
        self._injetables: Dict[str, Injectable] = {}
        self._controllers: Dict[str, Controller] = {}
        self._modules: Dict[str, Module] = {}
        self._intances = dict()
    
    def add_injectable(self, key: str, value: Any) -> None:
        self._injetables[key] = value
        
    def get_injectable(self, key) -> Optional[Any]:
        return self._injetables.get(key)
    
    def add_controller(self, key: str, value: Any) -> None:
        self._controllers[key] = value
        
    def get_controller(self, key) -> Optional[Any]:
        return self._controllers.get(key)
    
    def add_module(self, key: str, value: Any) -> None:
        self._modules[key] = value
        
    def get_module(self, key) -> Optional[Any]:
        return self._modules.get(key)
    
    
def class_name(obj: Any) -> str:
    return obj.__name__


tree = ArchonContainer()
