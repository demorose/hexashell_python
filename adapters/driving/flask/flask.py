from flask import Flask, render_template
from hex.domain.IReturnHelloWorld import helloWorld

def create_application():
    application = Flask(__name__)

    @application.route('/')
    def index():
        return render_template("index.j2", message=helloWorld())

    return application
