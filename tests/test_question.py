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
            response = self.post_question(1, "flask", "python", "importing files")
            print(response)
            self.assertTrue(response.content_type == 'application/json')

    def test_json_data_error_response(self):
        """
            Test error message if not json data provided
        """
        with self.client:
            response = self.post_question(1, "flask", "python", "importing files")
            data = json.loads(response.data.decode())
            self.assertNotEqual(data.get('message'), "Request should be json")

    def test_json_data_error_response_code(self):
        """
            Test response code if not json data provided
        """
        with self.client:
            response = self.post_question(1, "flask", "python", "importing files")
            self.assertNotEqual(response.status_code, 400)

    def test_question_added_successfully(self):
        """
            Test for successful posting of a questsion
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            response = self.post_question(1, "flask", "python", "importing files")
            self.assertEqual(response.status_code, 201)

    def test_auth_to_post_question(self):
        """
            Test for an 
            unathorized user can post a questsion
        """
        with self.client:
            response = self.post_question(1, "flask", "python", "importing files")
            data = json.loads(response.data.decode())
            self.assertEqual(data.get('message'), "Sign up to be able to ask questions  on this platform")
