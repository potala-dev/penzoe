.PHONY: local

local:
	heroku local

deploy:
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	git commit -q -a -m "deploy" 2>&1 1>/dev/null
	git push
	git push heroku master

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
    # sudo kill -9 $(sudo lsof -t -i:5432) 2>&1 1>/dev/null
	#docker stop penzoe_db
	#docker container stop $(docker container ls -q --filter name=penzoe_db*)
	docker start penzoe_db
	# docker run -p 5432:5432 \
	# 	-e POSTGRES_USER=postgres \
	# 	-e POSTGRES_PASSWORD=postgres \
	# 	-e POSTGRES_DB=db-dev \
	# 	-v ${PWD}/app_db:/var/lib/postgresql/data \
	# 	--name penzoe_db \
	# 	-d postgres:12

pgadmin:
	docker run -p 5050:80 \
		-e 'PGADMIN_DEFAULT_EMAIL=10zin@esukhia.org' \
		-e 'PGADMIN_DEFAULT_PASSWORD=openpecha' \
		-d dpage/pgadmin4
