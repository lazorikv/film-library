from app.app import db
from sqlalchemy.dialects.postgresql import INTEGER, SMALLINT, VARCHAR, TIMESTAMP, TEXT
from sqlalchemy.sql.schema import ForeignKeyConstraint, CheckConstraint
from datetime import datetime


class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(INTEGER, primary_key=True)
    name = db.Column(VARCHAR(255), nullable=False)
    rate = db.Column(SMALLINT, CheckConstraint('rate > 0 and rate <= 10'), nullable=False)
    year = db.Column(SMALLINT, CheckConstraint('year > 1880'), nullable=False)
    description = db.Column(TEXT)
    poster = db.Column(VARCHAR(255), nullable=False)
    director_id = db.Column(INTEGER, nullable=False)
    user_id = db.Column(INTEGER, nullable=False)
    ForeignKeyConstraint(
        ['director_id', 'user_id'],
        ['Director.id', 'User.id'],
        onupdate="CASCADE"
    )
    created = db.Column(TIMESTAMP, nullable=False, default=datetime.utcnow())

    def __init__(self, name, rate, year, description, image_link, d_id, u_id, date):
        self.name = name
        self.rate = rate
        self.year = year
        self.description = description
        self.poster = image_link
        self.director_id = d_id
        self.user_id = u_id
        self.created = date

    def __repr__(self):
        return f'Movie {self.name} {self.year} {self.rate}/10'
