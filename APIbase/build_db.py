import os
from config import db
from models import Entry

DATA = [
    {'temperature': 28, 'location': 'Paris'},
    {'temperature': 21, 'location': 'London'},
    {'temperature': 24, 'location': 'Athens'}
]
if os.path.exists('data.db'):
    os.remove('data.db')
    
db.create_all()

for entry in DATA:
    e = Entry(temperature=entry['temperature'], location=entry['location'])
    db.session.add(e)
    
db.session.commit()