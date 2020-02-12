from db import db
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True)
    password_hash = db.Column(db.String(128))
    car = db.relationship('Car', uselist=False)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), index=True)
    own_id = db.Column(db.String(30), db.ForeignKey('user.id'))
    own = db.relationship('User', uselist=False)
