run:
	python3 app.py

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf pydatagen/__pycache__

test:
	pytest

build:
	python3 -m build