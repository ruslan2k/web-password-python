PYTHON := env/bin/python


dev: dev.db
	${PYTHON} ./manage.py runserver 0.0.0.0:8000

prod: dev.db
	env/bin/gunicorn -b 0.0.0.0:8000 mysite.wsgi --log-file -

collectstatic:
	${PYTHON} ./manage.py collectstatic

requirements:
	apt-get install libpq-dev

env:
	virtualenv -p python3 env
	env/bin/pip install -r requirements.txt

dev.db:
	$(PYTHON) ./manage.py makemigrations resources 
	$(PYTHON) ./manage.py migrate

db_info:
	heroku addons | grep -i POSTGRES
	heroku config -s | grep DATABASE
	heroku pg:info

dump:
	heroku pg:backups:capture
	heroku pg:backups:download

local:
	heroku local web

push:
	git push heroku master

on:
	heroku ps:scale web=1

off:
	heroku ps:scale web=0

