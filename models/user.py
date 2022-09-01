from app import db


class User(db.Model):
    _tablname_ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(70), nullable=True)
    last_name = db.Column(db.String(70), nullable=True)
    Email = db.Column(db.String(70))
    password = db.Column(db.String(70))
    user_id = db.Column(db.Integer, nullable=True)
    name_title = db.Column(db.String(70), nullable=True)
    text_title = db.Column(db.Text, nullable=True)
    like = db.Column(db.Integer, nullable=True)
    dislike = db.Column(db.Integer, nullable=True)

    @property
    def serialize(self):
        return {
            'First name': self.first_name,
            'Last name': self.last_name,
            'Email': self.Email
        }
