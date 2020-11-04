default: install install-dev

help:
	@egrep '(^\S)|^$$' Makefile


install:
	pip install pip --upgrade
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt


# Apply Black formatting to Python files.
format:
	black .

# Lint with Pylint.
lint:
	# This doesn't work - cd boris && pylint *
	# But this does.
	export PYTHONPATH=boris && pylint boris


# Apply formatting and lint.
c check: format lint


tweet:
	boris/boris.py
