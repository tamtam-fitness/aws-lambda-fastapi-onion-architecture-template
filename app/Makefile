.PHONY: install, test, lint, format

install:
	docker exec app poetry install
test:
	docker exec app python3 -m poetry run pytest tests --cov=/var/task --cov-report term-missing

lint:
	docker exec app poetry run mypy --explicit-package-bases .
	docker exec app poetry run ruff check .
	docker exec app poetry run black --check .

format:
	docker exec app poetry run ruff check . --fix --exit-non-zero-on-fix
	docker exec app poetry run black .
