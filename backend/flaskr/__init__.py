import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Headers", "Authorization")
        response.headers.add("Access-Control-Allow-Headers", "true")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, PUT")
        response.headers.add("Access-Control-Allow-Methods", "PATCH, DELETE")
        response.headers.add("Access-Control-Allow-Methods", "OPTIONS")
        return response

    @app.route('/')
    def index():
        return jsonify({
            'success': True,
            'message': 'Welcome to Udacitytrivia'
        })

    @app.route('/questions', methods=['GET'])
    def get_questions():
        categories = Category.query.all()
        form_categories = [category.type.format() for category in categories]

        category = request.args.get('category', 1, int)
        current_category = Category.query.get(category)
        for_cat = current_category.type.format()

        page = request.args.get('page', 1, int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        questions = Question.query.filter(Question.category == current_category.id).all()

        formatted_questions = [question.format() for question in questions]

        if formatted_questions[start:end]:
            return jsonify({
                'success': True,
                'questions': formatted_questions[start:end],
                'total_questions': len(formatted_questions),
                'current_category': for_cat,
                'categories': form_categories
            })

        else:
            abort(404)

    @app.route('/categories', methods=['GET'])
    def get_categories():
        if request.method == 'GET':
            categories = Category.query.all()
            formatted_categories = [cat.type.format() for cat in categories]

            return jsonify({
                'success': True,
                'categories': formatted_categories
            })
        else:
            abort(405)

    @app.route('/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
        try:
            question = Question.query.get(id)
            db.session.delete(question)
            db.session.commit()

            return jsonify({
                'success': True,
                'message': '{id} is successfully deleted'
            })

        except question:
            abort(405)

    @app.route('/questions', methods=['POST'])
    def add_new_question():
        try:
            response = request.get_json()
            question = response.get('question')
            answer_text = response.get('answer')
            category = response.get('category')
            difficulty_score = response.get('difficulty')

            new_question = Question(question=question, answer=answer_text, category=category, difficulty=difficulty_score)

            db.session.add(new_question)
            db.session.commit()

            return jsonify({
                'success': True,
                'message': 'Question {new_question.id} successfully added'
            })

        except response:
            abort(400)

    @app.route('/questions/search', methods=['POST'])
    def find_questions():
        try:
            response = request.get_json()
            term = response.get('searchTerm')
            questions = Question.query.all()
            found_questions = []
            for question in questions:
                if term.lower() in question.question.lower():
                    found_questions.append(question.format())

            return jsonify({
                'success': True,
                'questions': found_questions
            })
        except response:
            abort(404)

    @app.route('/category/<int:category_id>/questions', methods=['POST', 'GET'])
    def questions_per_category(category_id):
        try:
            # to correct for index error from the frontend
            category_id = category_id + 1 

            # to cancel index error that may arise here in the backend:
            categories_number = Category.query.count()

            if category_id > categories_number:
                category_id = category_id - 1

            questions = Question.query.filter(Question.category == int(category_id)).all()
            formatted_questions = [question.format() for question in questions]

            if formatted_questions == []:
                return jsonify({
                    'success': False,
                    'message': 'No category_id ' + str(category_id),
                    'questions': formatted_questions
                }), abort(404)

            else:
                return jsonify({
                    'success': True,
                    'questions': formatted_questions,
                    'total_questions': len(formatted_questions),
                    'current_category': category_id
                })

        except:
            abort(404)

    @app.route('/quiz', methods=['POST'])
    def play_quiz():
        try:
            response = request.get_json()

            previous_questions = response.get('previous_questions')
            category_data = response.get('quiz_category')

            print(previous_questions)

            quiz_category = int(category_data['id']) + 1

            if category_data['type'] == 'click':
                questions = Question.query.all()
            else:
                questions = Question.query.filter(Question.category == quiz_category).all()

            formatted_questions = [question.format() for question in questions]

            for question in formatted_questions:
                if question['id'] in previous_questions:
                    formatted_questions.remove(question)

            current_question = random.choice(formatted_questions)

            return jsonify({
                'success': True,
                'question': current_question,
                'category': quiz_category
            })

        except:
            abort(500)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(405)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request'
        }), 400

    @app.errorhandler(500)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Server Error'
        }), 500

    return app
