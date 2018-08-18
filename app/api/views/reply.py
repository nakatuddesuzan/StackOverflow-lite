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
                    return jsonify(reply_made)   
        return jsonify({"message": "User not found"})   
    return jsonify({"message": "Sign up to reply"})

#endpoint for user to delete replies to his or her question
@answers.route('/api/v1/answers/<int:user_id>/<int:qtn_id>', methods=['DELETE'])
def delete_replies(user_id, qtn_id):
    for user in users_list:
            if user_id == user['user_id']:
                for question in qtns_list:
                    if qtn_id == question['qtn_id']:
                        replies_list.clear()
                        return jsonify({'Replies left': replies_list}) 
    return jsonify({'message': 'Oooppss something went wrong'})

# #endpoint for user to delete a reply to his or her question
@answers.route('/api/v1/answer/<int:user_id>/<int:qtn_id>/<int:reply_id>', methods=['DELETE'])
def delete_reply(user_id, qtn_id, reply_id):
    for count, user in enumerate(users_list):
            if user_id == user['user_id']:
                for count, question in enumerate(qtns_list):
                    if qtn_id == question['qtn_id']:
                        for count, reply in enumerate(replies_list):
                            if reply_id == reply['reply_id']:
                                replies_list.pop(count)
                                return jsonify({'Replies left': replies_list}) 
    return jsonify({'message': 'Oooppss something went wrong'})
