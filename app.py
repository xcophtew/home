from flask import Flask
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return 'Hello, World!'

@freezer.register_generator
def index():
    return '/'

if __name__ == '__main__':
    freezer.run()
