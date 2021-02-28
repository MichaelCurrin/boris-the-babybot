default: install install-dev

help:
	@grep '^[a-z]' Makefile


install:
	pip install pip --upgrade
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt


format:
	black .

lint:
	export PYTHONPATH=boris && pylint boris

fix: format lint


tweet:
	boris/boris.py
