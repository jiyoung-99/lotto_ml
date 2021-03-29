from app import db

class Lotto_his(db.Model):

    __tablename__ = "lotto_his"

    id = db.Column(db.Integer(), primary_key=True)
    date_l = db.Column(db.String(10), nullable=False)
    first_num = db.Column(db.Integer(), nullable=False)
    first_cnt = db.Column(db.String(20), nullable=False)
    sec_num = db.Column(db.Integer(), nullable=False)
    sec_cnt = db.Column(db.String(12), nullable=False)
    thd_num = db.Column(db.Integer(), nullable=False)
    thd_cnt = db.Column(db.String(10), nullable=False)
    one = db.Column(db.Integer(), nullable=False)
    two = db.Column(db.Integer(), nullable=False)
    three = db.Column(db.Integer(), nullable=False)
    four = db.Column(db.Integer(), nullable=False)
    five = db.Column(db.Integer(), nullable=False)
    six = db.Column(db.Integer(), nullable=False)
    bonus = db.Column(db.Integer(), nullable=False)


    def __repr__(self):
        return f'Lotto_his {self.id}'