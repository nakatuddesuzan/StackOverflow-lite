import re
from flask import jsonify
from app import app
from app import generate_id
from app.api.models.questions import Question, qtns_list

users_list = []

user_id = generate_id(users_list)


class User(Question):
    """Class representing User model"""

    def __init__(self, user_id, username, email, password):
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
        if len(pwd) < 8 and len(pwd) > 12:
            raise Exception(
                "Weak password \n Password must be 8 characters long ")
        if not re.search(r'[0-9]', pwd):
            raise Exception(
                'Weak password \n Password should have atleast one integer')
        if pwd.isupper() or pwd.islower() or pwd.isdigit():
            print(
                "Weak password \n Either you need to include alphabets or \n try include both letter cases")
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

