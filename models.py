from db import db
from passlib.apps import custom_app_context as pwd_context
from datetime import datetime
import shortuuid

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(30), primary_key=True, nullable=False,
                   default=shortuuid.uuid())
    username = db.Column(db.String(32), index = True)
    password_hash = db.Column(db.String(128))

    update_time = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    create_time = db.Column(db.DateTime, default=datetime.now)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.String(30), primary_key=True, nullable=False,
                   default=shortuuid.uuid())
    name = db.Column(db.String(32), index=True)
    own_id = db.Column(db.String(30), db.ForeignKey('user.id'))
    own = db.relationship('User', uselist=False,
                          backref=db.backref('car', uselist=False), )

    update_time = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    create_time = db.Column(db.DateTime, default=datetime.now)
