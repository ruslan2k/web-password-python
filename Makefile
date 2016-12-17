PYTHON:=env/bin/python

runserver: dev.db env
	env/bin/python ./manage.py runserver

env:
	virtualenv -p python3 env
	env/bin/pip install -r requirements.txt

dev.db:
	$(PYTHON) ./manage.py makemigrations resources 
	$(PYTHON) ./manage.py migrate

