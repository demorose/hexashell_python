from adapters.driving.flask import create_application
from hex.configure import configure_inject


def start():
    app = create_application()
    configure_inject()
    return app
