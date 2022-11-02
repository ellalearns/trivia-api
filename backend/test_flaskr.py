import os
import unittest
import json
from flask import jsonify
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
        self.database_path = 'postgresql://altx:altx@{}/{}'.format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_questions(self):
        res = self.client().get('/questions')
        self.assertEqual(res.status_code, 200)

    def test_get_questions_error(self):
        res = self.client().get('/questions?page=250')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        categories = Category.query.all()
        formatted_cats = [category.type.format() for category in categories]
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['categories'], formatted_cats)

    def test_get_categories_error(self):
        res = self.client().post('/categories')
        self.assertEqual(res.status_code, 405)

    def test_delete_question(self):
        question_ids = Question.query.all()
        ids = [question_id.id for question_id in question_ids]
        id = ids[-1]
        res = self.client().delete('/questions/' + str(id))
        self.assertEqual(res.status_code, 200)

    def test_delete_question_error(self):
        question_ids = Question.query.all()
        ids = [question_id.id for question_id in question_ids]
        id = ids[-1]
        res = self.client().post('/questions/' + str(id))
        self.assertEqual(res.status_code, 405)

    def test_add_new_question(self):
        test_q = json.dumps({'question': 'Who is my Queen?', 'answer': 'Mary', 'category': 3, 'difficulty': 1})
        headers = {'Content-Type': 'application/json'}
        res = self.client().post('/questions', data=(test_q), headers=headers)
        self.assertEqual(res.status_code, 200)

    def test_add_new_question_error(self):
        res = self.client().delete('/questions')
        self.assertEqual(res.status_code, 405)

    def test_find_question(self):
        data = json.dumps({'searchTerm': 'hank'})
        headers = {'Content-Type': 'application/json'}
        res = self.client().post('/questions/search', data=data, headers=headers)
        self.assertEqual(res.status_code, 200)

    def test_find_question_error(self):
        res = self.client().get('/questions/search')
        self.assertEqual(res.status_code, 405)

    def test_questions_per_category(self):
        res = self.client().post('/category/3/questions')
        data = json.loads(res.data)
        question_list = Question.query.filter(Question.category == 4).all()
        questions = [question.format() for question in question_list]
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['questions'], questions)

    def test_questions_per_category_error(self):
        res = self.client().post('/category/8/questions')
        self.assertEqual(res.status_code, 404)

    def test_play_quiz(self):
        data = json.dumps({'previous_questions': (), 'quiz_category': {'id': 3, 'type': 'Art'}})
        headers = {'Content-Type': 'application/json'}
        res = self.client().post('/quiz', data=data, headers=headers)
        self.assertEqual(res.status_code, 200)

    def test_play_quiz_error(self):
        res = self.client().post('/quiz')
        self.assertEqual(res.status_code, 500)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
