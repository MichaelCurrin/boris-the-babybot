help:
	@egrep '(^\S)|^$$' Makefile


# Install all dependencies.
install:
	pip install pip --upgrade
	pip install -r requirements.txt
	pip install -r requirements-dev.txt


# Apply Black formatting to Python files.
format:
	black .

# Lint with Pylint.
lint:
	pylint boris/

# Apply formatting and lint.
c check: format lint
