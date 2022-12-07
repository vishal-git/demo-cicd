test:
	pytest tests/test_image_clus.py

lint:
	flake8 src

bandit:
	bandit -r -lll src;

setup:
	pip install -r requirements.txt

setup-dev:
	pip install -r requirements-dev.txt

clean:
	rm -rf __pycache__
