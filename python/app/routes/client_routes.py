from flask import Blueprint, request
from app.services.client_service import add_client, get_clients, get_client_by_id, update_client, delete_client

client_bp = Blueprint('client_bp', __name__)

@client_bp.route('/clients', methods=['POST'])
def create_client():
    return add_client(request.json)

@client_bp.route('/clients', methods=['GET'])
def fetch_clients():
    return get_clients()

@client_bp.route('/clients/<string:id>', methods=['GET'])
def fetch_client_by_id(id):
    return get_client_by_id(id)

@client_bp.route('/clients/<string:id>', methods=['PUT'])
def modify_client(id):
    return update_client(id, request.json)

@client_bp.route('/clients/<string:id>', methods=['DELETE'])
def remove_client(id):
    return delete_client(id)
