from flask import Blueprint, request
from flasgger import swag_from
from app.services.client_service import get_logs, add_client, get_clients, get_client_by_id, update_client, delete_client

client_bp = Blueprint('client_bp', __name__)

@client_bp.route('/clients', methods=['POST'])
@swag_from({
    'tags': ['CRUD table client_dummy'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nama': {'type': 'string'},
                    'alamat': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Client successfully created'}
    }
})
def create_client():
    return add_client(request.json)

@client_bp.route('/clients', methods=['GET'])
@swag_from({
    'tags': ['CRUD table client_dummy'],
    'responses': {
        200: {
            'description': 'List of clients',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'string', 'format': 'uuid'},
                        'nama': {'type': 'string'},
                        'alamat': {'type': 'string'},
                        'created_time': {'type': 'string', 'format': 'date-time'}
                    }
                }
            }
        }
    }
})
def fetch_clients():
    return get_clients()

@client_bp.route('/apilogs', methods=['GET'])
@swag_from({
    'tags': ['Mengambil data table api_logs'],
    'responses': {
        200: {
            'description': 'List of apilogs',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'api_id': {'type': 'string', 'format': 'uuid'},
                        'request_payloads': {'type': 'json'},
                        'responnse_payloads': {'type': 'json'},
                        'created_time': {'type': 'string', 'format': 'date-time'}
                    }
                }
            }
        }
    }
})
def fetch_api():
    return get_logs()

@client_bp.route('/client/<int:uuid>', methods=['GET'])
@swag_from({
    'tags': ['CRUD table client_dummy'],
    'parameters': [
        {
            'name': 'id',
            'in': 'query',
            'type': 'string',
            'format': 'uuid',
            'required': True,
            'description': 'UUID of the client to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'Client details',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'format': 'uuid'},
                    'nama': {'type': 'string'},
                    'alamat': {'type': 'string'},
                    'created_time': {'type': 'string', 'format': 'date-time'}
                }
            }
        },
        404: {'description': 'Client not found'}
    }
})
def fetch_client_by_id():
    client_id = request.args.get('id')
    if not client_id:
        return {'message': 'ID is required'}, 400
    return get_client_by_id(client_id)

@client_bp.route('/clients', methods=['PUT'])
@swag_from({
    'tags': ['CRUD table client_dummy'],
    'parameters': [
        {
            'name': 'id',
            'in': 'query',
            'type': 'string',
            'format': 'uuid',
            'required': True,
            'description': 'UUID of the client to update',
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nama': {'type': 'string'},
                    'alamat': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Client successfully updated'},
        404: {'description': 'Client not found'}
    }
})
def modify_client():
    client_id = request.args.get('id')
    if not client_id:
        return {'message': 'ID is required'}, 400
    return update_client(client_id, request.json)

@client_bp.route('/clients', methods=['DELETE'])
@swag_from({
    'tags': ['CRUD table client_dummy'],
    'parameters': [
        {
            'name': 'id',
            'in': 'query',
            'type': 'string',
            'format': 'uuid',
            'required': True,
            'description': 'UUID of the client to delete',
        }
    ],
    'responses': {
        200: {'description': 'Client successfully deleted'},
        404: {'description': 'Client not found'}
    }
})
def remove_client():
    client_id = request.args.get('id')
    if not client_id:
        return {'message': 'ID is required'}, 400
    return delete_client(client_id)
