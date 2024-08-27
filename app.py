from flask import Flask
from frozen_flask import Frozen

app = Flask(__name__)
frozen = Frozen(app)

@app.route('/')
def index():
    return 'Hello, World!'

@frozen.register_generator
def index():
    return '/'

if __name__ == '__main__':
    frozen.run()
