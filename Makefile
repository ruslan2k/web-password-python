PYTHON:=venv/bin/python
TS:=$(shell date +%FT%T)

-include .env
export $(shell sed 's/=.*//' .env)

dev: dev.db
	${PYTHON} ./manage.py runserver 0.0.0.0:8000

prod: dev.db
	venv/bin/gunicorn -b 0.0.0.0:8000 mysite.wsgi --log-file -

collectstatic:
	${PYTHON} ./manage.py collectstatic

requirements:
	apt-get install libpq-dev

venv:
	virtualenv -p python3 venv
	venv/bin/pip install -r requirements.txt

dev.db: venv
	$(PYTHON) ./manage.py makemigrations resources 
	$(PYTHON) ./manage.py migrate

db_info:
	heroku addons | grep -i POSTGRES
	heroku config -s | grep DATABASE
	heroku pg:info

dump:
	pg_dump ${PGDATABASE} >> pg_dump.$(TS).sql
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

