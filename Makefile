.PHONY: local

local:
	heroku local

deploy:
	git push && git push heroku master

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

db:
	# sudo kill -9 $(sudo lsof -t -i:5432)
	docker run -p 5432:5432 \
		-e POSTGRES_USER=postgres \
		-e POSTGRES_PASSWORD=postgres \
		-e POSTGRES_DB=db-dev \
		-v ${PWD}/app_db:/var/lib/postgresql/data \
		-d postgres:12

pgadmin:
	docker run -p 5050:80 \
		-e 'PGADMIN_DEFAULT_EMAIL=10zin@esukhia.org' \
		-e 'PGADMIN_DEFAULT_PASSWORD=openpecha' \
		-d dpage/pgadmin4