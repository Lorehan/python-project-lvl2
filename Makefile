install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/*.whl

package-reinstall:
	python -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff