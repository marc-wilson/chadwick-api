from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class People(db.Model):
    __tablename__ = 'people'
    playerID = db.Column(db.String, primary_key=True)
    birthYear = db.Column(db.Integer)
    birthMonth = db.Column(db.Integer)
    birthDay = db.Column(db.Integer)
    birthCountry = db.Column(db.String)
    birthState = db.Column(db.String)
    birthCity = db.Column(db.String)
    deathYear = db.Column(db.Integer)
    deathMonth = db.Column(db.Integer)
    deathDay = db.Column(db.Integer)
    deathCountry = db.Column(db.String)
    deathState = db.Column(db.String)
    deathCity = db.Column(db.String)
    nameFirst = db.Column(db.String)
    nameLast = db.Column(db.String)
    nameGiven = db.Column(db.String)
    wieght = db.Column(db.Integer)
    height = db.Column(db.Integer)
    bats = db.Column(db.String)
    throws = db.Column(db.String)
    debut = db.Column(db.Date)
    finalGame = db.Column(db.Date)
    retroID = db.Column(db.String)
    bbrefID = db.Column(db.String)