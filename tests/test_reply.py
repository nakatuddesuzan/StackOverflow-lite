import json

from tests.base import BaseTestCase
from app.api.models.reply import Reply


class TestReplies(BaseTestCase):

    """Class for testing user replies"""
    
    def test_if_json_data(self):
        """
            Test for json data
        """
        with self.client:
            response = self.post_reply(1, 1, "Use static methods")
            self.assertTrue(response.content_type == 'application/json')
            
    def test_reply_class(self):
        """Test for existence of reply model"""
    
        reply = Reply(1, 1, 'install flask')
        self.assertTrue(reply)
    
    def test_json_data_error_response(self):
        """
            Test error message if not json data provided
        """
        with self.client:
            response = self.post_reply(1, 1, "Use static methods")
            data = json.loads(response.data.decode())
            self.assertNotEqual(data.get('message'), "Request should be json")
    
    def test_json_data_error_response_code(self):
        """
            Test response code if not json data provided
        """
        with self.client:
            response = self.post_reply(1, 1, "Use static methods")
            self.assertNotEqual(response.status_code, 400)

    def test_successful_replying(self):
        """
            Test for successful posting of 
            user repplies for a specific question
        """
        with self.client:

            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.post_question(1, "flask", "python", "importing files")
            response = self.post_reply(1, 1, "Use static methods")
            self.assertEqual(response.status_code, 200)

    def test_replying_to_non_existing_question(self):
        """Test for trying to replying 
            to a question that nolonger exists
        """
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            response = self.post_reply(1, 1, "Use static methods")
            data = json.loads(response.data.decode())
            self.assertEqual(data.get("message"), "User not found")
    
    def test_replying_by_non_existent_user(self):
        """
            Test for trying to replying to a question
            before signing up
        """
        with self.client:
            response = self.post_reply(1, 1, "Use static methods")
            data = json.loads(response.data.decode())
            self.assertEqual(data.get("message"), "Sign up to reply")
    
    def test_delete_reply(self):
        """Test  if a reply can be deleted"""
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.post_question(1, "flask", "python", "importing files")
            self.post_reply(1, 1, "Use static methods")
            response = self.delete_reply(1, 1, 1)
            data = json.loads(response.data.decode())
            self.assertEqual(data['Replies left'], [])

    def test_unauthorized_delete_of_a_reply(self):
        """Test if a non-registere user can delete a reply"""
        with self.client:
            self.post_question(1, "flask", "python", "importing files")
            self.post_reply(1, 1, "Use static methods")
            response = self.delete_reply(1, 1, 1)
            data = json.loads(response.data.decode())
            self.assertEqual(data['message'], 'Oooppss something went wrong')
        
    def test_delete_replies(self):
        """Test  if all replies can be deleted at once"""
        with self.client:
            self.register_user("sue", "sue@gmail.com", "Bootcamp11")
            self.post_question(1, "flask", "python", "importing files")
            self.post_reply(1, 1, "Use static methods")
            response = self.delete_all_replies(1, 1)
            data = json.loads(response.data.decode())
            self.assertEqual(data['Replies left'], [])

    def test_unauthorized_delete_of_all_replies(self):
        """Test if a non-registere user can delete a reply"""
        with self.client:
            self.post_question(1, "flask", "python", "importing files")
            self.post_reply(1, 1, "Use static methods")
            response = self.delete_all_replies(1, 1)
            data = json.loads(response.data.decode())
            self.assertEqual(data.get('message'), 'Oooppss something went wrong')
    
    def test_get_all_replies(self):
        with self.client:
            self.post_question(1, "flask", "python", "importing files")
            self.post_reply(1, 1, "Use static methods")
            response = self.get_all_replies(1)
            self.assertEqual(response.status_code, 200)
    
    def test_test_get_replies_for_a_non_existent_question(self):
        with self.client:
            response = self.get_all_replies(1)
            data = json.loads(response.data.decode())
            print(data)
            self.assertEqual(data['message'], 'No replies found')