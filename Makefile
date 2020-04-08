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
	pylint boris

	# OR for better import recognition but lack of working file links in lint
	# output.
	#cd boris && pylint *

# Apply formatting and lint.
c check: format lint
