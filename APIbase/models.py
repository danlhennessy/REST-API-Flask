from config import db, ma

class Entry(db.Model):
    __tablename__ = 'entry'
    entry_id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer, index=True)
    location = db.Column(db.String(32))

class EntrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Entry
        load_instance = True