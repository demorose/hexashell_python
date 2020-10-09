from adapters.driving.flask.flask import application
from configure import configure_inject

if __name__ == "__main__":
    configure_inject()
    application.run()
