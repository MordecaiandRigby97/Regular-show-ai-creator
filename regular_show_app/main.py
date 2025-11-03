"""Command line interface for the Regular Show inspired creator app."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

from .characters import Character, default_characters, list_voice_actors
from .movie_maker import MovieProject, create_default_project
from .story import Scene, babysitting_story
from .video_generator import assemble_video, export_project


def describe_characters(characters: List[Character]) -> str:
    return "\n\n".join(character.describe() for character in characters)


def describe_story(scenes: List[Scene]) -> str:
    return "\n\n".join(scene.summarize() for scene in scenes)


def run_cli() -> None:
    parser = argparse.ArgumentParser(
        description="Create a Regular Show style mini-movie with outfits and voice actors.",
    )
    parser.add_argument(
        "--export",
        type=Path,
        help="Directory to export the storyboard and generated frames.",
    )
    parser.add_argument(
        "--assemble",
        type=Path,
        help="Optional destination file to stitch generated frames into a pseudo-video.",
    )
    args = parser.parse_args()

    characters = default_characters()
    scenes = babysitting_story()
    project = create_default_project()

    print("=== Voice Actors Featured ===")
    for actor in list_voice_actors():
        print(f" - {actor}")
    print()

    print("=== Character Profiles ===")
    print(describe_characters(characters))
    print()

    print("=== Story Beats ===")
    print(describe_story(scenes))
    print()

    print("=== Movie Maker Storyboard ===")
    print(project.storyboard())

    if args.export:
        storyboard_path = export_project(project, args.export)
        print(f"\nExported storyboard to {storyboard_path}")
        frames_dir = args.export / "frames"
        if args.assemble:
            frame_files = sorted(frames_dir.glob("scene_*.txt"))
            assemble_video(frame_files, args.assemble)
            print(f"Assembled pseudo-video at {args.assemble}")


if __name__ == "__main__":
    run_cli()
