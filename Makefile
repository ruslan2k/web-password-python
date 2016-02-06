SHELL := bash

include .env

default: composer.lock
	php artisan serve

composer.lock: composer.json
	time composer update

vendor/autoload.php:
	time composer install

composer.json: vendor/autoload.php

dump:
	mysqldump -h${DB_HOST} -u${DB_USERNAME} -p${DB_PASSWORD} ${DB_DATABASE}  --extended-insert=FALSE   | less
