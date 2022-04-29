.PHONY: install format lint test sec docs main

install:
	@poetry install

format:
	@poetry run isort .
	@poetry run blue .

lint:
	@poetry run blue . --check
	@poetry run isort . --check
	@poetry run prospector --with-tool pydocstyle --doc-warning --no-autodetect
	
test:
	@poetry run pytest -v

sec:
	@poetry run pip-audit

docs:
	@poetry run mkdocs serve

main:
	@python ttdiagnosis/main.py -$(arg)