from app import db
from uuid import uuid4
from datetime import datetime
from sqlalchemy import text

class ApiLog(db.Model):
    __tablename__ = 'api_logs'
    api_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    request_payloads = db.Column(db.Text, nullable=False)
    response_payloads = db.Column(db.Text, nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
