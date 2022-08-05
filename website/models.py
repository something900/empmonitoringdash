from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class Empreview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empid = db.Column(db.String(10))
    jobknowledge = db.Column(db.String(10))
    workquality = db.Column(db.String(10))
    workquality = db.Column(db.String(10))
    attendence = db.Column(db.String(10))
    communication = db.Column(db.String(10))
    dependability = db.Column(db.String(10))
    comments = db.Column(db.String(800))
    date=db.Column(db.DateTime(timezone=True), default=func.now())
    #when doing forign key, use simple letter to reference
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    #add into empreview table
    empreviews = db.relationship('Empreview')