# project setup
RUN: git clone  https://github.com/gloriouscomputer/djangoproject.git
Create virtualenvioriment in python3.11
RUN: Python3.11 -m venv myenv
RUN: source myenv/bin/activate

(myenv):python manage.py migrate
(myenv):python manage.py runserver
it will run on default server(http://127.0.0.1.0:8000)

