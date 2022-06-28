run:
	python ./src/main.py ${file}

install:
	pip install -r ./requirements.txt

tests: install
	python -m pytest --cov-report term --cov=src tests/
