# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 
```
Endpoints
GET '/categories'
GET '/questions'
GET '/questions/<int:question_id>'
POST '/questions'
DELETE '/questions'

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Sample: curl http://127.0.0.1:5000/categories 
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET '/questions'
- Fetches a dictionary questions, which consists of an Array, every dictionary then beeing one question. The questions are paginated by groups of 10 beginning with page 1 or /questions. The keys are the question´s properties and the values are the corresponding strings of the property
- Sample: curl http://127.0.0.1:5000/questions 
- Request Arguments: None
- Returns: An array of objects with 5 keys. 
{'answer' : "",
'category' : "",
'difficulty' : "",
'id' : "",
'question' : ""}

GET '/questions/<int:question_id>'
- Fetches a dictionary of one question in which the keys are the single properties and the values are the corresponding strings of the object
- Sample: curl http://127.0.0.1:5000/questions/2 
- Request Arguments: question_id
- Returns: An object with five keys. 
{'answer' : "",
'category' : "",
'difficulty' : "",
'id' : "",
'question' : ""}

GET '/categories/<int:category_id>/questions'
- Fetches a dictionary questions, which consists of an Array, every dictionary then beeing one question. The questions are selected per chosen category.
- Sample: curl http://127.0.0.1:5000/categories/2/questions
- Returns: An object of an array of the questions.
{
"current_category": "",
"questions": [
{
"answer": "",
"category": "",
"difficulty": "",
"id": "",
"question": ""
}
]
}

POST '/questions'
- Method, that accepts 
    - input per object consisting of question, answer, difficulty, category 
    - or a searchteam, that will be matched with the answer 
- Sample: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"Why", "answer":"Therefore", "category":"6", "difficulty":"42"}' 
- Allows a dictionary made of: "question", "answer", "category", "difficulty" or a string for the searchterm 

POST '/categories'
- Method, that accepts input per object consisting of type
- Allows a dictionary made of: "type"
- Sample: curl http://127.0.0.1:5000/categories -X POST -H "Content-Type: application/json" -d '{"id":"7", "type":"Humor"}' 

POST '/quizzes'
- Method, that accepts input per object consisting of quiz_questions or quiz_categories
- Allows a dictionary made of: "quiz_questions" or a number from 1-6 which is the id of the chosen category
- Sample: curl -d '{"quiz_questions"="4", "quiz_category"="2"}' -H "Content-Type: application/x-www-form-urlencoded" -X POST

DELETE '/questions'
- Method, that accepts input per object id
- Sample: curl -X DELETE http://127.0.0.1:5000/questions?id=2 
- Allows path to the specific object:
 /questions/<int:question_id>
 
PATCH 'questions'
- Method, that accepts input per question
- Sample: curl http://127.0.0.1:5000/questions/2 -X PATCH -H "Content-Type: application/json" -d '{"difficulty":"2"}' 
- Allows a dictionary made of: "question", "answer", "category", "difficulty"

ERRORHANDLING
Errors will be returned for example as: 
{
'success': False,
'error': 404,
'message': 'Resource not found'
}
The API will return types of error, when requests fail:
- 404: Resource not found.
- 422: Unprocessable.
- 400: Bad request.
- 405: Method not allowed.

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## Contribution
I found useful help not only in the Udacity Class Videos, but also in these Knowledge Questions:
[234306](https://knowledge.udacity.com/questions/234306) 
[246041](https://knowledge.udacity.com/questions/246041)
[207019](https://knowledge.udacity.com/questions/207019)
and in using [Pep8online](http://pep8online.com) for checking formatting Python as mentioned by reviewer 