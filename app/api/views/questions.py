from flask import Blueprint, request, jsonify, make_response
from app.api.models.user import users_list
from app.api.models.questions import Question, qtns_list
from app.api.models.user import User
from app import generate_id
from app.api.models.reply import Reply


questions = Blueprint('questions', __name__)
answers = Blueprint('answers', __name__)

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
        return jsonify(qtn_made), 200
    return jsonify({"message": "Sign up to be able to ask questions  on this platform"})

@answers.route('/api/v1/answer/<int:user_id>/<int:qtn_id>', methods=['POST'])
def post_answer(user_id, qtn_id):
    if not request.get_json():
        return make_response(jsonify({"message": "Request should be json"}), 400)
    reply_desc = request.get_json()['reply_desc']
    user_id = request.get_json()['user_id']
    qtn_id = request.get_json()['qtn_id']
    for user in  users_list:
        if user_id == user['user_id']:
            for question in qtns_list:
                if qtn_id == question['qtn_id']:
                    answer = Reply(user_id=user_id, qtn_id=qtn_id, reply_desc = reply_desc)
                    reply_made = User.make_reply(answer)
                    return jsonify(reply_made), 200   
        return jsonify({"message": "Question not "})   
    return jsonify({"message": "Sign up to be able to ask questions  on this platform"})
