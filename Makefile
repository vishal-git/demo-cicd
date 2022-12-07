test:
	pytest tests/test_image_clus.py

lint:
	flake8 src

bandit:
	bandit -r -lll src;
