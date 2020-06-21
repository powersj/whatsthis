# This file is part of whatsthis. See LICENSE file for license information.

build: clean
	python3 setup.py build

clean:
	python3 setup.py clean
	rm -rf .pytest_cache build dist *.egg-info .coverage 
	@find . -regex '.*\(__pycache__\|\.py[co]\)' -delete

install: clean
	pip install -r requirements.txt
	python3 setup.py install

publish: clean
	rm -rf dist/
	python3 setup.py sdist
	pip install twine
	twine upload dist/*

test:
	black --check .
	flake8 --max-line-length=88 whatsthis setup.py
	py.test --cov=whatsthis whatsthis

venv:
	python3 -m virtualenv venv
	venv/bin/pip install -Ur requirements.txt -Ur requirements-test.txt
	@echo "Now run the following to activate the virtual env:"
	@echo ". venv/bin/activate"

.PHONY: build clean install publish test venv
