import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = 'postgres://postgres:djurdjica@localhost:5432/trivia_test'
        setup_db(self.app, self.database_path)
        
        self.new_question = {
            'question_id': 1001,
            'question': 'Why? Warum? Hvorfor?',
            'answer': 'Therefore! Darum! Derfor!',
            'category': '2',
            'difficulty': '5' 
        }
        
        self.new_category = {
            'type': 'Humoreske'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_welcome_message(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['Welcome to Trivia API'])
    
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['categories'])
    
    def test_get_single_category(self):
        res = self.client(category_id).get('categories/4')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['category'])
        
    def test_404_sent_requesting_non_existing_category(self):
        res = self.client().get('/categories/?category_id=1200', json={'id': 1200})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found.')
    
    def test_get_questions(self):        
        res = self.client().get('/questions')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['questions'])
        self.assertEqual(data['total_questions'])
    
    def test_get_single_question(self):
        res = self.client(questions_id).get('/questions/2')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['question'])
        
    def test_post_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['created'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        
    def test_405_if_creation_not_allowed(self):
        res = self.client().post('/questions/500', json=self.new_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed.')
        
    def test_post_category(self):        
        res = self.client().post('/categories', json=self.new_category)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['categories']))
        
    def test_405_if_creation_not_allowed(self):
        res = self.client().post('/categories/500', json=self.new_category)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed.')
        
    def test_delete_question(self):    
        res = self.client().delete('/questions/1')
        data = json.loads(res.data)
        
        question = Question.query.filter(Question.id == 1).one_or_none()
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(['success'], True)
        self.assertEqual(data['deleted'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertEqual(question, None)
    
    def test_404_if_question_does_not_exist(self):
        res = self.client().delet('/questions/1200')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(datra['succes'], False)
        self.assertEqual(data['message'], 'Unprocessable.')
        
    def test_update_questions(self):    
        res = self.client().patch('/questions/3', json={'difficulty': 3})
        data = json.loads(res.data)
        question = Question.query.filter(Question.id == 3).one_or_none() 
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(question.format()['difficulty'], 3)
        
    def test_400_sent_requesting_update_on_question(self):
        res = self.client().patch('/questions/3')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request.')
        
    def test_filter_questions_by_category(self):
        res = self.client().post('/categories/1/questions', json={'search': 'category' == 1})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertEqual(len(data['questions']), 3)
        
    def test_filter_questions_by_category_fails(self):
        res.self.client().post('/categories/1000/questions', json={'search': 'category' == 1000})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], 0)
        self.assertEqual(len(data['questions']), 0)
       
    def test_play_the_quiz(self):
        res = self.client().post('/play', json={'previous_questions': [6], 'quiz_category': {'id': 3}})
        data = json.loads(res.data)
        
        self.assertTrue(data['question'])
        self.assertEqual(res.status_code, 200)
        
    def test_play_the_quiz_fails(self):
        res = self.client().post('/play', json={'previous_questions': None, 'quiz_category': None})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'Unprocessable.')
                

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
