"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum


""" Created a model called `Guest` with the following fields:
    id: primary key
    name: String column
    email: String column
    phone: String column
    events_attending: relationship to "Event" table with a secondary table
"""
class Guest(db.Model):
    """Guest model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(12), unique=True, nullable=False)

    events_attending = db.relationship('Event', secondary='guest_event', back_populates='guests')

""" Created a model called `Event` with the following fields:
    id: primary key
    title: String column
    description: String column
    date_and_time: DateTime column
    guests: relationship to "Guest" table with a secondary table
"""
# STRETCH CHALLENGE: 
"""Added a field `event_type` as an Enum column that denotes the
type of event (Party, Study, Networking, etc)
"""
class Event_type(enum.Enum):
    PARTY = 'Party'
    STUDY = 'Study'
    NETWORKING = 'Networking'
    Generic = 'Generic'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(200))
    date_and_time = db.Column(db.DateTime)

    # The type - What type of event it is?s
    event_type = db.Column(db.Enum(Event_type), default=Event_type.Generic)

    guests= db.relationship('Guest', secondary='guest_event', back_populates='events_attending')

    def __str__(self):
        return f'<User: {self.title}>'

    def __repr__(self):
        return f"""<{self.id}: {self.title}>"""

""" table `guest_event_table` with the following columns:
    event_id: Integer column (foreign key)
    guest_id: Integer column (foreign key)
"""

guest_event = db.Table('guest_event',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

guest_event_table = None