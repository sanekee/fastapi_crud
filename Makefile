.PHONY: init
init:
	alembic revision --autogenerate -m "initial migration"
	alembic upgrade head

.PHONY: seed
seed:
	python seed.py
