import jwt
from datetime import datetime, timedelta
import re
from flask import jsonify
from app import app
from app import generate_id
from app.api.models.questions import Question, qtns_list
from app.api.models.reply import Reply, replies_list

users_list = []

user_id = generate_id(users_list)


class User(Question , Reply):
    """Class representing User model"""

    def __init__(self, user_id, username, email, password):
        super(User, self). __init__(user_id, 'title', 'subject', 'qtn_desc')
        super(User, self). __init__(user_id, 'qtn_id', 'reply_desc','qtn_dec')
        self.user_id = generate_id(users_list)
        self.username = username
        self.email = email
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        if not pwd:
            raise Exception("Field can't be empty")
        if len(pwd) < 8 or len(pwd) > 12:
            raise Exception(
                "Weak password \n Password must be 8 characters long ")
        if not re.search(r'[0-9]', pwd):
            raise Exception(
                'Weak password \n Password should have atleast one integer')
        if pwd.isupper() or pwd.islower() or pwd.isdigit():
            print("Weak password")
        self._password = pwd

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise Exception("Email field can't be empty")
        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", value):
            raise ValueError('Enter Valid Email ID forexample "sue@gmail.com"')
        self._email = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value:
            raise Exception("Field can't be empty")
        if len(value) <= 2:
            raise Exception("Name too sort \n  Not allowed")
        if re.compile('[!@#$%^&*:;?><.0-9]').match(value):
            raise ValueError("Invalid characters not allowed")

        self._username = value

    def create_qtn(self):
        new_qtn = {
            "qtn_id": self.qtn_id,
            "title": self.title,
            "subject": self.subject,
            "qtn_desc": self.qtn_desc 
        }

        qtns_list.append(new_qtn)
        return new_qtn

    @staticmethod
    def update_qtn(qtn_id, user_id, title, subject, qtn_desc):
        """This method enables a user to update question by id"""
        for user in users_list:
            if user_id == user['user_id']:
                for question in qtns_list:
                    if qtn_id == question['qtn_id']:
                        question['title'] = title
                        question['subject'] = subject
                        question['qtn_desc'] = qtn_desc
                        return question
        return {"message": "OOOOooooppps something went wrong"}

    @staticmethod
    def delete_qtn(qtn_id, user_id):
        """This method enables a user to delete question by id"""
        for count, user in enumerate(users_list):
            if user_id == user['user_id']:
                for count, question in enumerate(qtns_list):
                    if qtn_id == question['qtn_id']:
                        qtns_list.pop(count)
                        return qtns_list     
        return qtns_list
      
    def make_reply(self):
        new_reply =  {
            "qtn_id": self.qtn_id,
            "user_id": self.user_id,
            "reply": self.reply_desc  
        }
        replies_list.append(new_reply)
        return new_reply
      
    @staticmethod
    def get_one_question(qtn_id):
        """This method gets a question from a list of questions"""
        for  question in qtns_list:
            if qtn_id == question['qtn_id']:
                return question
        return {"message": "question not found"}


    @staticmethod
    def get_questions():
        """
            This method returns all questions on the platform
        """
        if qtns_list:
            return jsonify({"User Requests": qtns_list})
        return jsonify({"message": "No questions found"})
        
    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            """ set payload expiration time"""
            payload = {
                #expiration date of the token
                'exp': datetime.utcnow() + timedelta(seconds=30),
                # international atomic time
                #the time the token is generated
                'iat': datetime.utcnow(),
                # the subject of the token 
                # (the user whom it identifies)
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return {'user_id': payload['sub'], "status": "Success"}
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'