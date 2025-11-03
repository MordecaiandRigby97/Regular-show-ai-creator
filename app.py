"""Command line interface for generating Regular Show fan content ideas."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from typing import Any, Callable, Dict

from regular_show_app import (
    FanArtPrompt,
    FanMoviePlot,
    FanVideoPlan,
    generate_fan_art_prompt,
    generate_fan_movie_plot,
    generate_fan_video_plan,
)

GENERATOR_MAP: Dict[str, Callable[[int], Any]] = {
    "art": generate_fan_art_prompt,
    "video": generate_fan_video_plan,
    "movie": generate_fan_movie_plot,
}

DEFAULT_COUNTS = {
    "art": 2,
    "video": 3,
    "movie": 4,
}


def _format_output(result: FanArtPrompt | FanVideoPlan | FanMoviePlot, as_json: bool) -> str:
    if as_json:
        return json.dumps(asdict(result), indent=2)

    if isinstance(result, FanArtPrompt):
        return (
            f"Title: {result.title}\n"
            f"Characters: {', '.join(result.characters)}\n"
            f"Description: {result.description}"
        )
    if isinstance(result, FanVideoPlan):
        scenes = "\n - ".join(result.scenes)
        return (
            f"Hook: {result.hook}\n"
            f"Featured Characters: {', '.join(result.featured_characters)}\n"
            f"Scenes:\n - {scenes}"
        )
    scenes = "\n - ".join(result.acts)
    return (
        f"Synopsis: {result.synopsis}\n"
        f"Starring: {', '.join(result.starring)}\n"
        f"Acts:\n - {scenes}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "medium",
        choices=sorted(GENERATOR_MAP.keys()),
        help="Type of fan content to generate",
    )
    parser.add_argument(
        "--characters",
        type=int,
        help="Number of characters to include",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Return the output as JSON",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    generator = GENERATOR_MAP[args.medium]
    count = args.characters if args.characters is not None else DEFAULT_COUNTS[args.medium]
    result = generator(count)
    print(_format_output(result, as_json=args.json))


if __name__ == "__main__":
    main()
