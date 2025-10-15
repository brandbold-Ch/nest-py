from fastapi.routing import APIRoute
from nest_py.common import ctx


class LoggingRoute(APIRoute):

    def get_route_handler(self):
        original_route_handler = super().get_route_handler()
        
        async def custom_route_handler(request, *args, **kwargs):
            scope = self.endpoint
            
            if hasattr(scope, "_route"):
                controller = scope._route.controller
                
                for name, anno in controller.__annotations__.items():
                    setattr(ctx, name, anno())
                    
            response = await original_route_handler(request, *args, **kwargs)
            return response
        
        return custom_route_handler
