run:
	python3 pygendata/cli/__init__.py --generate csv --base json tests/test.json --to tests/test_json_out.csv --rows 10

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
