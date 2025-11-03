# Regular Show AI Creator

This project is a playful command line experience that imagines a movie maker and video generator
built around the voice actors of *Regular Show*. It focuses on Sydney asking Janie to babysit her
daughter Emily Rose while she directs a new park commercial, only to have the messy prankster Jayla
crash the set. The app highlights outfits, accessories, dramatic tension, and a pseudo video
production pipeline.

## Features

- Character profiles featuring Regular Show voice actors and unique outfits
- Jayla's chaotic arrival, complete with messy accessories and a resolution arc with Janie
- A movie maker storyboard complete with voice lines from the cast
- A mock video generator that exports ASCII "frames" and assembles them into a stitched document

## Getting Started

Create a virtual environment (optional) and install the project in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

> The project has no external dependencies, so the installation step simply makes the package
> importable from anywhere inside the virtual environment.

## Usage

Run the CLI to print the character descriptions, story beats, and storyboard. By default the
command also exports a storyboard, frames, and an assembled "video" to `exports/latest`:

```bash
python -m regular_show_app
```

Use `--export` to choose a different directory, or `--assemble` to override the assembled
file name. Pass `--skip-export` if you only want console output without writing any files:

```bash
python -m regular_show_app --export out/project --assemble out/video.txt
```

If you install the package with `pip install -e .`, the convenience command
`regular-show-creator` is also available:

```bash
regular-show-creator --skip-export
```

## Tests

Execute the unit tests with `pytest`:

```bash
pytest
```
