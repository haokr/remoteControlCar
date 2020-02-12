from flask import Flask, render_template
import api
from auth import auth

app = Flask(__name__)

app.register_blueprint(api.car.view, url_prefix="/api/car")
app.register_blueprint(api.user.view, url_prefix="/api/user")


@auth.login_require
@app.before_request
def before_request():
    pass

if __name__ == '__main__':
    app.run()
