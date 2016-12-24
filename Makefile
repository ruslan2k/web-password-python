PYTHON:=env/bin/python

runserver:
	gunicorn -b 0.0.0.0:8000 mysite.wsgi --log-file -
	#env/bin/python ./manage.py runserver

collectstatic:
	env/bin/python ./manage.py collectstatic

requirements:
	apt-get install libpq-dev

env:
	virtualenv -p python3 env
	env/bin/pip install -r requirements.txt

dev.db: env
	$(PYTHON) ./manage.py makemigrations resources 
	$(PYTHON) ./manage.py migrate

local:
	heroku local web

push:
	git push heroku master

on:
	heroku ps:scale web=1

off:
	heroku ps:scale web=0
