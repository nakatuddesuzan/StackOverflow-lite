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
    
    def test_get_all_questions(self):
        """test if user can retrieve all questions"""

        with self.client:
            self.post_question(1, "flask", "python", "importing files")
            self.post_question(1, "flask", "python", "importing files")
            response = self.get_all_questions()
            self.assertEqual(response.status_code, 200)

    def test_retrieve_one_questions(self):
        """test if user can retrieve one question"""

        with self.client:
            self.post_question(1, "flask", "python", "importing files")
            response = self.get_one_question()
            self.assertEqual(response.status_code, 200)

    def test_delete_question(self):
        """test if user can delete one question"""

        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.post_question(1, "flask", "python", "importing files")
            response = self.delete_question(1, 1)
            self.assertEqual(response.status_code, 200)
    
    def test_update_question(self):
        """test if user can update a question"""

        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.post_question(1, "flask", "python", "importing files")
            response = self.update_question(1, 1, "not working", "CSS", "chjushxhxbh" )
            print(response)
            self.assertEqual(response.status_code, 200)

    def test_json_data_error_response_for_update_question(self):
        """
            Test error message if not json data provided
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.post_question(1, "flask", "python", "importing files")
            response = self.update_question(1, 1, "not working", "CSS", "chjushxhxbh" )
            data = json.loads(response.data.decode())
            self.assertNotEqual(data.get('message'), "Request should be json")

    def test_json_data_error_response_code_for_update_question(self):
        """
            Test response code if not json data provided
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.post_question(1, "flask", "python", "importing files")
            response = self.update_question(1, 1, "not working", "CSS", "chjushxhxbh" )
            self.assertNotEqual(response.status_code, 400)

    def test_post_question_by_non_existent_user(self):
        """Test for an authorized questions posting"""

        with self.client:
            response = self.post_question(1, "flask", "python", "importing files")
            data = json.loads(response.data.decode())
            self.assertEqual(
                data.get('message'), 
                "Sign up to be able to ask questions  on this platform"
                )

