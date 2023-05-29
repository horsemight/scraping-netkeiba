.PHONY: setup
setup:
	python -m pip install -U pip
	python -m pip install -U poetry

.PHONY: install
install:
	poetry install

.PHONY: sync
sync:
	poetry install --sync

.PHONY: test
test:
	poetry run pytest ./tests

.PHONY: test-ci
test-ci:
	poetry run pytest ./tests -sv --junit-xml results/pytest.xml

.PHONY: fmt
fmt:
	poetry run black .

.PHONY: fmt-ci
fmt-ci:
	poetry run black . --check 2>&1 | sed -n '/would reformat .*/p' | sed 's/would reformat \(.*\)/\1/g'

.PHONY: ci
ci: setup sync
