default: install install-dev

all: install install-dev fmt-check lint


h help:
	@grep '^[a-z]' Makefile


install:
	pip install pip --upgrade
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

upgrade:
	pip install pip --upgrade
	pip install -r requirements.txt --upgrade
	pip install -r requirements-dev.txt --upgrade


fmt:
	black .
fmt-check:
	black . --diff --check
lint:
	export PYTHONPATH=boris && pylint boris

fix: fmt lint


tweet:
	boris/boris.py
