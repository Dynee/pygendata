run:
	python3 pydatagen.py --generate csv --base ddl tests/users.txt --to tests/users.csv --rows 100

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf pydatagen/__pycache__

test:
	pytest

build:
	python3 -m build