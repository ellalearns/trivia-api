# TRIVIA API -- Ella Agu & Udacity
Trivia API is a project about an online Udacity quiz. 
Players can select categories, answer questions, and see their final score.
Developers can access the API to request a list of questions, categories, and questions per category.

All backend code follows PEP8 style guidelines.

Basic file structure looks like this:

_ Backend

___ flaskr

_____ __init__.py

___ test_flaskr.py

___ models.py

___ trivia.psql

_ Frontend

_ README_ella_agu.md




# To Begin


## Pre-requisites and Local Setup
Ensure you have Python 3, pip, node, and npm already installed on your local machine.


### Backend
A list of dependencies have been provided in the requirements.txt

To install all dependencies in bash, command prompt, and powershell:

```
pip install -r requirements.txt
```

**We recommend that you work within a virtual environment to keep project dependencies organized**

#### To run the backend server

**For Command Prompt and Powershell**

```
set FLASK_APP=flaskr
set FLASK_DEBUG=1
flask run
```

**For GitBash**

``
export FLASK_APP=flaskr
export FLASK_DEBUG=1
flask run
``

The __init__.py file will run by default. To run the test server first, use the command: ```set FLASK_APP=test_flaskr```

The application runs on ```http://127.0.0.1:5000/``` and is a proxy to the frontend. 


### Frontend

Ensure that the node_modules folder are present in the frontend folder.

Run the following commands to start the frontend.

``` 
npm install (if it's not installed yet)
set node_options=--openssl-legacy-provider
npm start
```

The application runs on ```http://127.0.0.1:3000/``` by default.



## Testing

To run tests, navigate to the backend folder in your terminal. Run the following command:

```
python test_flaskr.py
```


## API Reference

**Base URL**

```
http://127.0.0.1:5000/
```

No authentication is required.

### EndPoints

#### GET /questions

&emsp;*General*

&emsp;&emsp;Returns a list of questions, categories, and total number of questions.

&emsp;&emsp;Result is in form of a json object.

&emsp;&emsp;Questions are limited to 10 per page.
    
&emsp;*Sample*

&emsp;&emsp;```curl http://127.0.0.1:5000/questions```

&emsp;&emsp;
```json
{
"categories": [
"Science",
"Art",
"Geography",
"History",
"Entertainment",
"Sports"
],
"current_category": "Science",
"questions": [
{
"answer": "Maya Angelou",
"category": 4,
"difficulty": 2,
"id": 5,
"question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
},
{
"answer": "Muhammad Ali",
"category": 4,
"difficulty": 1,
"id": 9,
"question": "What boxer's original name is Cassius Clay?"
},
{
"answer": "Apollo 13",
"category": 5,
"difficulty": 4,
"id": 2,
"question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
},
{
"answer": "Tom Cruise",
"category": 5,
"difficulty": 4,
"id": 4,
"question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
},
{
"answer": "Edward Scissorhands",
"category": 5,
"difficulty": 3,
"id": 6,
"question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
},
{
"answer": "Brazil",
"category": 6,
"difficulty": 3,
"id": 10,
"question": "Which is the only team to play in every soccer World Cup tournament?"
},
{
"answer": "Uruguay",
"category": 6,
"difficulty": 4,
"id": 11,
"question": "Which country won the first ever soccer World Cup in 1930?"
},
{
"answer": "George Washington Carver",
"category": 4,
"difficulty": 2,
"id": 12,
"question": "Who invented Peanut Butter?"
},
{
"answer": "Lake Victoria",
"category": 3,
"difficulty": 2,
"id": 13,
"question": "What is the largest lake in Africa?"
},
{
"answer": "The Palace of Versailles",
"category": 3,
"difficulty": 3,
"id": 14,
"question": "In which royal palace would you find the Hall of Mirrors?"
}
],
"success": true,
"total_questions": 49
}
```


#### GET /categories

&emsp;*General*

Returns a list of categories

&emsp;*Sample*

```curl http://127.0.0.1:5000/categories```

```json
{
  "categories": [
    "Science",
    "Art",
    "Geography",
    "History",
    "Entertainment",
    "Sports"
  ],
  "success": true
}
```

#### DELETE /questions/<int:id>

&emsp;*General*

Deletes a queestion using the id. Returns a json response.

&emsp;*Sample*

```curl -X DELETE http://127.0.0.1:5000/questions/23```

```json
{
  "message": "{id} is successfully deleted",
  "success": True
}
```

#### POST /questions

&emsp;*General*

Adds a question after receiving a json request. 

&emsp;*Sample*

```curl -H "Content-Type: application/json" -X POST -d '{"question":"Who is my Queen?","answer":"Mary","category":3,"difficulty":1}' http://127.0.0.1:5000/questions```

```json
{
  "message": "Question {new_question.id} successfully added",
  "success": true
}
```

#### POST /questions/search

&emsp;*General*

Returns the questions containing the search term.

&emsp;*Sample*

```curl -H "Content-Type: application/json" -X POST -d '{"searchTerm":"hank"}' http://127.0.0.1:5000/questions/search```

```json
{
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }
  ],
  "success": true
}
```

#### POST /category/<int:category_id>/questions

&emsp;*General*

Returns a list of questions in a category.

&emsp;*Sample*

```curl -X POST http://127.0.0.1:5000/category/2/questions```

```json
{
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true
}
```

#### POST /quiz

&emsp;*General*

Returns a random quiz question from a category.

&emsp;*Sample*

```curl -H "Content-Type: application/json" -X POST -d '{"previous_questions":[],"quiz_category":3}' http://127.0.0.1:5000/quiz```

```json
{
  "category": 2,
  "question": {
    "answer": "One",
    "category": 2,
    "difficulty": 4,
    "id": 18,
    "question": "How many paintings did Van Gogh sell in his lifetime?"
  },
  "success": true
}
```

### Error Handling

All errors are returned in json format. 

#### 400

&emsp;*Sample*

```curl -X POST -d "json{'question': 'Who is my Queen?', 'answer': 'Mary', 'category': 3, 'difficulty': 1}" -H 'Content-Type: application/json' http://127.0.0.1:5000/questions```

```json
{
  "error": 400,
  "message": "Bad Request",
  "success": false
}
```

#### 404

&emsp;*Sample*

```curl -X POST http://127.0.0.1:5000/category/27/questions```

```json
{
  "error": 404,
  "message": "Resource not found",
  "success": false
}
```

#### 405

&emsp;*Sample*

```curl -X POST http://127.0.0.1:5000/questions/26```

```json
{
  "error": 405,
  "message": "Method Not Allowed",
  "success": false
}
```

#### 500

&emsp;*Sample*

```curl -X POST http://127.0.0.1:5000/quiz```

```json
{
  "error": 500,
  "message": "Server Error",
  "success": false
}
```

## Authors

Ella Agu
Udacity

## Thanks!










