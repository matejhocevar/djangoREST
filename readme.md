# django REST
Simple django rest application for demostration and learning purposes
Built with [django rest framework](http://www.django-rest-framework.org/)
<br>
<br>

### Prerequisites

##### Libraries
	virtualenv
	pip
	django
<br>

##### Database
This project use internal SQLite database, so there is no need for database setup. If you want to change database you can do it in settings.py file.
<br>
<br>

### Installation

##### Create virtual enviroment
	virtualenv env  
<br>

##### Activate virtual enviroment
on Windows:
	cd env/Scripts
	activate

on Unix:
	source env/bin/activate
<br>

##### Install dependencies:
	pip install -r requirements.txt
<br>

##### Migrate database:
	python manage.py migrate
<br>
<br>

### Usage:

##### Run server:
	python manage.py runsever <ip:port>	# example: python manage.py runserver 127.0.0.1:8000
<br>

##### REST API:
Django REST framework offers their own REST api via browser:
	http://127.0.0.1:8000/snippets/
	
<br>

##### Requests with httpie library:
	http http://127.0.0.1:8000/snippets/
	http http://127.0.0.1:8000/users/ Accept:text/html
	http http://127.0.0.1:8000/snippets.json
	http http://127.0.0.1:8000/users.api
<br>

##### Using HTTP methods:
	http <GET | POST | PUT | DELETE | OPTIONS | HEAD	http://127.0.0.1:8000/snippets/
<br>

##### Post using form data:
	http --form POST http://127.0.0.1:8000/snippets/ code="print 123"
<br>

##### Post using JSON:
	http --json POST http://127.0.0.1:8000/snippets/ code="print 456"
<br>

##### Using authentication:
	http -a matej:password POST http://127.0.0.1:8000/snippets/ code="print 789"
<br>
<br>

### Author
Matej Hocevar [@matoxxx](https://github.com/matoxxx)

