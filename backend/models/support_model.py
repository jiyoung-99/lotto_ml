from app import db


class Support(db.Model):
    __tablename__ = 'support'
    id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)

    def __repr__(self):
        return f'Support {self.id}'
