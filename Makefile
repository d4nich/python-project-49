build:
	uv build

package-install:
	python3 -m pip install --user dist/*.whl

install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

lint:
	uv run ruff check brain_games
