run:
	python3 pygendata/__init__.py --generate csv --base ddl tests/users.txt --to tests/users.csv --rows 100

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf pygendata/__pycache__
	rm -rf dist/*
	rm tests/output.csv tests/users.csv tests/united_states_points.csv tests/united_states_points.json

test:
	pytest

build:
	python3 -m build
