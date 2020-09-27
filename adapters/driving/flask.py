from flask import Flask
from hex.domain.IReturnHelloWorld import main

def create_application():
    application = Flask(__name__)

    @application.route('/')
    def index():
        return main()

    return application
