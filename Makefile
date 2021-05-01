manage_py := python manage.py

runserver:
	$(manage_py) runserver 127.0.0.1:8000

flake8:
	flake8 ./catalogs
	flake8 ./yalantis

migrate:
	$(manage_py) migrate