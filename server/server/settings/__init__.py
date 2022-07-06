import os

ENVIRONMENT = os.environ.get("ENVIRONMENT")

match ENVIRONMENT:

    case "staging":
        pass

    case "production_web":
        pass

    case _:
        from .dev import *
