.PHONY: migratedb
migratedb:
	alembic upgrade head

.PHONY: seed
seed:
	python seed.py
