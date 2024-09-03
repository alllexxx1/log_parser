run:
	python manage.py runserver

lint:
	poetry run flake8

tests:
	python manage.py test

compose-up:
	docker-compose up --build

check: tests lint
