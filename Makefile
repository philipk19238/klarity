build: 
	docker-compose build
down:
	docker-compose down --remove-orphans
up:
	docker-compose up
migrate:
	-docker-compose run --rm api flask db init
	docker-compose run --rm api flask db migrate
	docker-compose run --rm api flask db upgrade
