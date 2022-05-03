from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return {'user': '好的6678'}


if __name__ == '__main__':
    app.run()
