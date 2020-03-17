import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_storeSingle_response(self):
        self.my_survey.save_response(self.responses[0])
        self.assertIn('English', self.my_survey.responses)

    def test_storeThree_responses(self):
        for response in self.responses:
            self.my_survey.save_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
