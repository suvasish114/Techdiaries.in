# database modeles
from . import db

# class User(db.Model):
#     __tablename__ = 'TD_user'
#     id = db.Column(db.Integer, primary_key = True)
#     email = db.Column(db.String(20))
#     password = db.Column(db.Integer)

#     def __repr__(self):
#         return '< email: '+self.email+' user id: '+self.id+' >'

class Admin(db.Model):
    __tablename__ = 'TD_admin'
    id = db.Column(db.Integer, primary_key = True)
    admin_id = db.Column(db.String(20))
    admin_password = db.Column(db.String(20))

    def __repr__(self):
        return '<admin_id: '+self.admin_id+', password: '+self.admin_password+'>'