# Regular Show AI Creator

This project is a playful command line experience that imagines a movie maker and video generator
built around the voice actors of *Regular Show*. It focuses on Sydney asking Janie to babysit her
daughter Emily Rose while she directs a new park commercial. The app highlights outfits, accessories,
and a pseudo video production pipeline.

## Features

- Character profiles featuring Regular Show voice actors and unique outfits
- Story beats that follow Sydney, Janie, and Emily Rose through their babysitting adventure
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

Run the CLI to print the character descriptions, story beats, and storyboard:

```bash
python -m regular_show_app.main
```

You can also export the storyboard and frames, and optionally assemble the pseudo video:

```bash
python -m regular_show_app.main --export out/project --assemble out/video.txt
```

## Tests

Execute the unit tests with `pytest`:

```bash
pytest
```
