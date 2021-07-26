# database modeles
from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.column(db.Integer, primary_key = True)
    email = db.column(db.String(20), unique = True)

    def __repr__(self):
        return '< email: '+self.email+' user id: '+self.id+' >'