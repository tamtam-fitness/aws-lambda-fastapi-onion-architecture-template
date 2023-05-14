.PHONY: install, test, lint, format

install:
	docker-compose exec app poetry install
test:
	docker-compose exec app python3 -m poetry run pytest tests --cov=/var/task --cov-report term-missing

lint:
	docker-compose exec app poetry run mypy --explicit-package-bases .
	docker-compose exec app poetry run ruff check .

format:
	docker-compose exec app poetry run ruff check . --fix --exit-non-zero-on-fix
	docker-compose exec app poetry run black .
