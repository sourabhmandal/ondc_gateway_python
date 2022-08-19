 ## run the API server
.PHONY: run
run:
	python3 manage.py runserver

.PHONY: migrate
migrate:
	python3 manage.py migrate