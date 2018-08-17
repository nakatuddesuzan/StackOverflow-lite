from flask import Blueprint, request, jsonify, make_response
from app.api.models.user import users_list
from app.api.models.questions import Question, qtns_list
from app.api.models.user import User
from app import generate_id
from app.api.models.reply import Reply, replies_list


answers = Blueprint('answers', __name__)


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
                    replies_list.append(reply_made)
                    return jsonify(reply_made)   
        return jsonify({"message": "Question not found"})   
    return jsonify({"message": "Sign up to be able to ask questions  on this platform"})