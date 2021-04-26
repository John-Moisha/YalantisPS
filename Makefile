manage_py := python manage.py

runserver:
	$(manage_py) runserver 0:8000

flake8:
	flake8 ./catalogs
	flake8 ./yalantis