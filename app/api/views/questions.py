from flask import Blueprint, request, jsonify, make_response
from app.api.models.user import users_list
from app.api.models.questions import Question, qtns_list
from app.api.models.user import User
from app import generate_id


questions = Blueprint('questions', __name__)

@questions.route('/api/v1/questions/<int:user_id>', methods=['POST'])
def post_question(user_id):
    if not request.get_json():
        return make_response(jsonify({"message": "Request should be json"}), 400)
    title = request.get_json()['title']
    subject = request.get_json()['subject']
    qtn_desc = request.get_json()['qtn_desc']
    user_id = request.get_json()['user_id']
    for user in users_list:
        if user['user_id'] == user_id:
            qtn_instance = Question(
                title=title,
                subject=subject,
                qtn_desc=qtn_desc,
                user_id=user_id
            )
        qtn_made = User.create_qtn(qtn_instance)
        return jsonify(qtn_made), 201
    return jsonify({"message": "Sign up to be able to ask questions  on this platform"}), 401

@questions.route('/api/v1/questions', methods=['GET'])
def get_all_questions():
    questions = User.get_questions()
    return questions

@questions.route('/api/v1/questions/<int:user_id>/<int:qtn_id>', methods=['PUT'])
def edit_question(user_id, qtn_id):
    if not request.get_json():
        return make_response(jsonify({"message": "Request should be json"}), 400)
    title = request.get_json()['title']
    subject = request.get_json()['subject']
    qtn_desc = request.get_json()['qtn_desc']
    user_id = request.get_json()['user_id']

    updated_qtn = User.update_qtn(
        qtn_id,
        title = title,
        subject = subject,
        qtn_desc = qtn_desc,
        user_id = user_id

    )
    
    return jsonify({'Updated': updated_qtn}), 200

@questions.route('/api/v1/questions/<int:user_id>/<int:qtn_id>', methods=['DELETE'])
def del_qtn(qtn_id, user_id):
    remaining_questions = User.delete_qtn(qtn_id, user_id)
    return jsonify({'Current_questions': remaining_questions})

@questions.route('/api/v1/question/<int:qtn_id>', methods=['GET'])
def get_question(qtn_id):
    question = User.get_one_question(qtn_id)
    return jsonify({qtn_id: question})

