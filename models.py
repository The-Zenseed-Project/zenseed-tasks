from extensions import db

class Programme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

class Subproject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    programme_id = db.Column(db.Integer, db.ForeignKey('programme.id'), nullable=False)

class NextAction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(256), nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    context = db.Column(db.String(64))
    subproject_id = db.Column(db.Integer, db.ForeignKey('subproject.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)
