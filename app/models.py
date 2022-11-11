from .extensions import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(10000))
    frequency = db.Column(db.String(100))
    dow = db.Column(db.String(100))
    month = db.Column(db.String(100))
    date = db.Column(db.String(100))
    hour = db.Column(db.String(100))
    minute = db.Column(db.String(100))
    am_pm = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')
