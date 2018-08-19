import json
from tests.base import BaseTestCase
from app.api.models.questions import Question


class TestQuestion(BaseTestCase):


    def test_if_questions_class_exists(self):
        question = Question(1, "flask", "python", "importing files")
        self.assertTrue(question)
        
    def test_if_json_data(self):
        """
            Test for json question data
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            response = self.login_user("sue@gmail.com", "Bootcamp11")
            token = self.get_token()
            response = self.post_question(token,  1,"flask", "python", "importing files")
            self.assertTrue(response.content_type == 'application/json')

    def test_json_data_error_response(self):
        """
            Test error message if not json data provided
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            response = self.login_user("sue@gmail.com", "Bootcamp11")
            token = self.get_token()
            response = self.post_question(token,  1,"flask", "python", "importing files")
            data = json.loads(response.data.decode())
            self.assertNotEqual(data.get('message'), "Request should be json")

    def test_json_data_error_response_code(self):
        """
            Test response code if not json data provided
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            response = self.login_user("sue@gmail.com", "Bootcamp11")
            token = self.get_token()
            response = self.post_question(token,  1,"flask", "python", "importing files")
            self.assertNotEqual(response.status_code, 400)

    def test_question_added_successfully(self):
        """
            Test for successful posting of a questsion
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            response = self.login_user("sue@gmail.com", "Bootcamp11")
            token = self.get_token()
            response = self.post_question(token,  1,"flask", "python", "importing files")
            self.assertEqual(response.status_code, 201)

    def test_auth_to_post_question(self):
        """
            Test for an 
            unathorized user can post a questsion
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            response = self.login_user("sue@gmail.com", "Bootcamp11")
            token = self.get_token()
            response = self.post_question(token,  1,"flask", "python", "importing files")
            data = json.loads(response.data.decode())
            self.assertEqual(data.get('message'),"Invalid token. Please log in again.")

    def test_get_all_questions(self):
        """test if user can retrieve all questions"""

        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.login_user("sue@gmail.com", "Bootcamp11")
            token = self.get_token()
            self.post_question(token,  1, "flask", "python", "importing files")
            response = self.get_all_questions(token)
            data = json.loads(response.data.decode())
            print(data)
            self.assertEqual(response.status_code, 200)

    def test_retrieve_one_questions(self):
        """test if user can retrieve one question"""

        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.login_user("sue@gmail.com", "Bootcamp11")
            token = self.get_token()
            self.post_question(token,  1, "flask", "python", "importing files")
            response = self.get_one_question(token)
            self.assertEqual(response.status_code, 200)

    def test_delete_question(self):
        """test if user can delete one question"""

        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.login_user("sue@gmail.com", "Bootcamp11")
            token = self.get_token()
            self.post_question(token,  1, "flask", "python", "importing files")
            response = self.delete_question(token, 1, 1)
            self.assertEqual(response.status_code, 200)
    
    def test_update_question(self):
        """test if user can update a question"""

        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.login_user("sue@gmail.com", "Bootcamp11")
            token = self.get_token()
            self.post_question(token,  1, "flask", "python", "importing files")
            response = self.update_question(token, 1, 1, "not working", "CSS", "chjushxhxbh" )
            self.assertEqual(response.status_code, 200)

    def test_json_data_error_response_for_update_question(self):
        """
            Test error message if not json data provided
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.login_user("sue@gmail.com", "Bootcamp11")
            token = self.get_token()
            self.post_question(token,  1, "flask", "python", "importing files")
            response = self.update_question(token, 1, 1, "not working", "CSS", "chjushxhxbh" )
            data = json.loads(response.data.decode())
            self.assertNotEqual(data.get('message'), "Request should be json")

    def test_json_data_error_response_code_for_update_question(self):
        """
            Test response code if not json data provided
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.login_user("sue@gmail.com", "Bootcamp11")
            token = self.get_token()
            self.post_question(token,  1, "flask", "python", "importing files")
            response = self.update_question(token, 1, 1, "not working", "CSS", "chjushxhxbh" )
            self.assertNotEqual(response.status_code, 400)
