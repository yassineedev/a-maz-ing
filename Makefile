install:
	pip install flake8 mypy

run:
	python3 a_maze_ing.py config.txt


debug:
	python3 -m pdb a_maze_ing config.txt

bild:
	cp dist/mazegen_bogido-0.0.1-py3-none-any.whl .
	cp dist/mazegen_bogido-0.0.1.tar.gz .
	rm -rf dist
clean:
	rm -rf __pycache__

lint:
	python3 -m flake8 .
	
lint-strict:
	python3 -m flake8 .
	python3 -m mypy . --strict

.PHONY: install run debug clean lint lint-strict
