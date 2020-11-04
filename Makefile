default: install install-dev

help:
	@egrep '(^\S)|^$$' Makefile


install:
	pip install pip --upgrade
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt


format:
	black .

lint:
	export PYTHONPATH=boris && pylint boris

c check: format lint


tweet:
	boris/boris.py
