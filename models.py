from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    # content = db.Column(db.String(200), nullable=False)
    # completed = db.Column(db.Integer, default=0)
    # date_created = db.Column(db.DateTime, default=db.func.now())

    # def __repr__(self):
    #     return '<Task %r>' % self.id

db.create_all()
    