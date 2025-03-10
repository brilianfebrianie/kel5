from app import db
from app.models.log import ApiLog
import json

def log_api(request_data, response_data):
    log_entry = ApiLog(
        request_payloads=json.dumps(request_data, default=str),
        response_payloads=json.dumps(response_data, default=str)
    )
    db.session.add(log_entry)
    db.session.commit()
