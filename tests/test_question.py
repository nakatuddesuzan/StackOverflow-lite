import json
from tests.base import BaseTestCase


class TestQuestion(BaseTestCase):
    def test_if_json_data(self):
        """
            Test for json question data
        """
        with self.client:
            response = self.post_question(1, "flask", "python", "importing files")
            self.assertTrue(response.content_type == 'application/json')

    def test_question_added_successfully(self):
        """
            Test for successful posting of a questsion
        """
        response = self.post_question(1, "flask", "python", "importing files")
        self.assertEqual(response.status_code, 200)

    def test_auth_to_post_question(self):
        """
            Test for an 
            unathorized user can post a questsion
        """
        response = self.post_question(1, "flask", "python", "importing files")
        data = json.loads(response.data.decode())
        self.assertEqual(data.get('message'), "Sign up to be able to ask questions  on this platform")
