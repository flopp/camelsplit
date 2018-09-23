PY_FILES=\
	./camelsplit/__init__.py \
	./camelsplit/camelsplit.py \
	./camelsplit/tests/__init__.py \
	./camelsplit/tests/test_basic.py

codespell: $(PY_FILES)
	codespell $(PY_FILES)

flake8: $(PY_FILES)
	flake8 $(PY_FILES)

pytest: $(PY_FILES)
	pytest --cov=camelsplit ./camelsplit
