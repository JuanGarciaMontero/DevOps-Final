from app import db


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    g
    def __repr__(self):
        return f"<Data id={self.id} name={self.name}>"