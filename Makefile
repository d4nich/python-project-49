build:
	uv build

package-install:
	python3 -m pip install --user dist/*.whl

install:
	uv sync

brain-games:
	uv run brain-games
