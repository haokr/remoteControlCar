from flask import Flask, render_template
import api
from auth import auth
import config
from db import db
from socket_io import socketio


app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)
socketio.init_app(app)

app.register_blueprint(api.car.car, url_prefix="/api/car")
app.register_blueprint(api.user.user, url_prefix="/api/user")


@auth.login_required
@app.before_request
def before_request():
    pass

if __name__ == '__main__':
    socketio.run(app)
