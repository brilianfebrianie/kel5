from flask import Blueprint, request
from flasgger import swag_from
from app.services.client_service import add_client, get_clients, get_client_by_id, update_client, delete_client

client_bp = Blueprint('client_bp', __name__)

@client_bp.route('/clients', methods=['POST'])
@swag_from({
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

@client_bp.route('/client', methods=['GET'])
@swag_from({
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
