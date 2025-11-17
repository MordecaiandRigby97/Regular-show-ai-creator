"""Command line interface for building Regular Show inspired stories."""

from __future__ import annotations

import argparse

from .movie_maker import MovieMaker
from .video_maker import VideoMaker


def build_video_example() -> str:
    video = VideoMaker(
        title="Park After Hours",
        premise="The crew scrambles to finish a viral video before sunrise.",
    )
    video.add_scene(
        "Mordecai and Rigby beg Sydney Jayla for last-minute sound fixes.",
        ["Mordecai", "Rigby", "Sydney Jayla"],
    )
    video.add_scene(
        "Emily Rose captures behind-the-scenes chaos while Jaylan pitches new bits.",
        ["Emily Rose", "Jaylan"],
    )
    video.add_scene(
        "Benson inspects the final cut as Skips delivers wise advice.",
        ["Benson", "Skips"],
    )
    return video.build_outline()


def build_movie_example() -> str:
    movie = MovieMaker(
        title="Regular Show: Multitrack Mayhem",
        logline=(
            "When Sydney Jayla uncovers a portal hidden in the park's audio booth,"
            " the gang dives into alternate soundscapes to save their universe."
        ),
    )
    movie.add_act(
        "Act I: The Glitched Track",
        [
            "Sydney Jayla finds a corrupted tape that remixes reality.",
            "Mordecai and Rigby enlist Emily Rose to document the phenomenon.",
            "Jaylan's sketches predict the crew's next destination.",
        ],
    )
    movie.add_act(
        "Act II: Feedback Frenzy",
        [
            "Skips and Benson lead the rescue mission through musical dimensions.",
            "Muscle Man and High Five Ghost improvise a bass drop battle.",
            "Jaylan teams up with Pops to calm the soundstorm.",
        ],
    )
    movie.add_act(
        "Act III: Harmony Restored",
        [
            "Emily Rose edits the definitive cut that seals the portal.",
            "Sydney Jayla conducts the final mix with the entire cast.",
            "The park celebrates with a premiere screening under the stars.",
        ],
    )
    return movie.build_outline()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode",
        choices={"video", "movie"},
        help="Select which example outline to generate.",
    )
    args = parser.parse_args()

    if args.mode == "video":
        print(build_video_example())
    else:
        print(build_movie_example())


if __name__ == "__main__":
    main()
