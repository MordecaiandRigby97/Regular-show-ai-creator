# Regular Show Fan Content Generator

Create prompts for fan art, videos, and movies inspired by *Regular Show*. This lightweight Python app
helps you brainstorm creative projects featuring Mordecai, Rigby, and the rest of the park crew.

## Features

- 🎨 **Fan art prompts** with characters, props, and locations.
- 📹 **Short-form video outlines** including hooks and scene beats.
- 🎬 **Three-act fan movie plots** ready for storyboarding.
- 🧪 **Tested** with `pytest` to ensure consistent outputs.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # optional if you install pytest for testing
```

The generators only rely on the standard library. Install `pytest` if you want to run the tests.

## Usage

Generate ideas directly from the command line:

```bash
python app.py art --characters 3
python app.py video --json
python app.py movie
```

Example output:

```
$ python app.py art
Title: Mordecai's Cosmic Portrait
Characters: Mordecai, Rigby
Description: Illustrate Mordecai, Rigby hanging out at the park while experimenting with a giant sandwich. Capture the show's surreal humor and vibrant color palette.
```

The `--json` flag returns structured output that you can feed into other tools or pipelines.

## Running Tests

```bash
pytest
```

## Extending

- Add more characters, locations, or props in `regular_show_app/data.py`.
- Customize templates in `regular_show_app/generator.py` for different storytelling styles.
- Build a web or GUI frontend on top of `app.py` to share fan creations.
