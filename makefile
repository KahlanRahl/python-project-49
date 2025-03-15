install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	flake8 brain_games

.PHONY: install brain-games build package-install lint