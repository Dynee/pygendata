run:
	python3 pygendata.py --generate csv --base ddl tests/users.txt --to tests/users.csv --rows 100

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf pygendata/__pycache__
	rm -rf dist/*

test:
	pytest

build:
	python3 -m build