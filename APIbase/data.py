from flask import make_response, abort
from config import db
from models import Entry, EntrySchema

def display_all():
    entry = Entry.query.order_by(Entry.entry_id).all()  # Gets all Entry class data and orders by entry_id
    entry_schema = EntrySchema(many=True)  # Preps Marshmallow to serialize
    data = entry_schema.dump(entry)  # Serialize data for JSON output
    return data