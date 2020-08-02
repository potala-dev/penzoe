.PHONY: local

local:
	heroku local

graph:
	./manage.py graph_models \
		core \
		courses \
		schools \
		students \
		users \
		-o models.png

coverage:
	coverage run -m pytest --migrations
	coverage report

mypy:
	mypy penzoe manage.py