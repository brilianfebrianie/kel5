from app import db
from uuid import uuid4
from datetime import datetime

class ClientDummy(db.Model):
    __tablename__ = 'client_dummy' 
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    nama = db.Column(db.String(255), nullable=False)
    alamat = db.Column(db.String(255), nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.utcnow)