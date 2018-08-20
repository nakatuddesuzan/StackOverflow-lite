from functools import wraps
from flask_restful import abort
from flask import request, jsonify, g
from app.api.models.user import User
from app.api.models.questions import qtns_list, Question

def login_required(func):
    """
    login_required. protects a route to only authenticated users
    """
    @wraps(func)
    def auth(*args, **kwargs):
        access_token = request.headers.get('token')
        if access_token is None:
            return jsonify({"message": "No token, please provide a token"}), 401
        if access_token:
            user_id = User.decode_auth_token(access_token)
            if not isinstance(user_id, str):
                return func(user_id,*args,**kwargs)
            return jsonify({'message': user_id}),401
    return auth
