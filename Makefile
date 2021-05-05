manage_py := python manage.py

runserver:
	$(manage_py) runserver 127.0.0.1:8000

flake8:
	flake8 ./catalogs
	flake8 ./yalantis

migrate:
	$(manage_py) migrate

runtest:
	pytest

build:
	docker-compose up -d

show_project:
	python -m webbrowser http://127.0.0.1:8000


run_project: build migrate runserver