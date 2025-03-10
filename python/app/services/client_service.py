from app import db
from app.models.client import ClientDummy
from app.utils.logger import log_api
from flask import jsonify

def add_client(data):
    new_client = ClientDummy(nama=data['nama'], alamat=data['alamat'])
    db.session.add(new_client)
    db.session.commit()
    response = {'message': 'Client added successfully', 'id': new_client.id}
    log_api(data, response)
    return jsonify(response), 201

def get_clients():
    clients = ClientDummy.query.all()
    result = [{'id': c.id, 'nama': c.nama, 'alamat': c.alamat, 'created_time': c.created_time.isoformat()} for c in clients]
    log_api({}, result)
    return jsonify(result)

def get_client_by_id(id):
    client = ClientDummy.query.get(id)
    if not client:
        response = {'message': 'Client not found'}
        log_api({'id': id}, response)
        return jsonify(response), 404
    
    result = {'id': client.id, 'nama': client.nama, 'alamat': client.alamat, 'created_time': client.created_time.isoformat()}
    log_api({'id': id}, result)
    return jsonify(result)

def update_client(id, data):
    client = ClientDummy.query.get(id)
    if not client:
        response = {'message': 'Client not found'}
        log_api({'id': id}, response)
        return jsonify(response), 404
    
    client.nama = data.get('nama', client.nama)
    client.alamat = data.get('alamat', client.alamat)
    db.session.commit()
    
    response = {'message': 'Client updated successfully', 'id': client.id}
    log_api(data, response)
    return jsonify(response)

def delete_client(id):
    client = ClientDummy.query.get(id)
    if not client:
        response = {'message': 'Client not found'}
        log_api({'id': id}, response)
        return jsonify(response), 404
    
    db.session.delete(client)
    db.session.commit()
    
    response = {'message': 'Client deleted successfully'}
    log_api({'id': id}, response)
    return jsonify(response)
