"""Regular Show voice actor creative generator.

Allows generating song arrangements, movie concepts, and fan video ideas
featuring the Regular Show voice cast plus original character Sydney.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import argparse
import json
from typing import List, Dict, Any

VOICE_CAST: Dict[str, str] = {
    "Mordecai": "J.G. Quintel",
    "Rigby": "William Salyers",
    "Benson": "Sam Marin",
    "Pops": "Sam Marin",
    "Muscle Man": "Sam Marin",
    "Skips": "Mark Hamill",
    "Hi Five Ghost": "J.R. Villarreal",
    "Eileen": "Minty Lewis",
    "CJ": "Linda Cardellini",
    "Margaret": "Janie Haddad Tompkins",
}

SYDNEY = {
    "name": "Sydney",
    "hair": "orange",
    "eyes": "green",
    "description": "Sydney sports bright orange hair, vibrant green eyes, and loves backing up the crew with killer harmonies.",
}


def available_characters() -> str:
    lines = ["Available Regular Show voice actors:"]
    for character, actor in VOICE_CAST.items():
        lines.append(f"- {character}: voiced by {actor}")
    lines.append(
        f"- {SYDNEY['name']}: original character with {SYDNEY['hair']} hair and {SYDNEY['eyes']} eyes."
    )
    return "\n".join(lines)


@dataclass
class SongArrangement:
    title: str
    lead: str
    background: List[str] = field(default_factory=list)
    vibe: str = "uplifting synthwave"
    tempo_bpm: int = 120

    def describe(self) -> str:
        backers = ", ".join(self.background) if self.background else "(solo)"
        return (
            f"Song: {self.title}\n"
            f"- Lead vocals: {self.lead}\n"
            f"- Background vocals: {backers}\n"
            f"- Vibe: {self.vibe} at {self.tempo_bpm} BPM\n"
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "lead": self.lead,
            "background": self.background,
            "vibe": self.vibe,
            "tempo_bpm": self.tempo_bpm,
        }


def build_song(args: argparse.Namespace) -> str:
    lead = args.lead or "Mordecai"
    background = args.background or ["Rigby", "Sydney"]
    arrangement = SongArrangement(
        title=args.title,
        lead=lead,
        background=background,
        vibe=args.vibe,
        tempo_bpm=args.tempo,
    )
    output = [arrangement.describe(), available_characters()]
    if args.json:
        output.append("\nJSON blueprint:\n" + json.dumps(arrangement.to_dict(), indent=2))
    return "\n".join(output)


@dataclass
class FanVideo:
    title: str
    theme: str
    setting: str
    spotlight: str = SYDNEY["name"]

    def outline(self) -> str:
        return (
            f"Fan video: {self.title}\n"
            f"- Theme: {self.theme}\n"
            f"- Setting: {self.setting}\n"
            f"- Spotlight character: {self.spotlight} ({SYDNEY['description']})\n"
            f"- Cameos: {', '.join(list(VOICE_CAST.keys())[:4])}\n"
        )


def build_fan_video(args: argparse.Namespace) -> str:
    video = FanVideo(title=args.title, theme=args.theme, setting=args.setting)
    return video.outline()


@dataclass
class MoviePitch:
    title: str
    antagonist: str
    hook: str
    finale_song: SongArrangement

    def synopsis(self) -> str:
        return (
            f"Movie pitch: {self.title}\n"
            f"- Antagonist: {self.antagonist}\n"
            f"- Hook: {self.hook}\n"
            f"- Finale Song ->\n{self.finale_song.describe()}"
        )


def build_movie(args: argparse.Namespace) -> str:
    finale = SongArrangement(
        title=args.finale_title,
        lead=args.finale_lead or "Sydney",
        background=args.finale_background or ["Mordecai", "Rigby", "Skips"],
        vibe=args.finale_vibe,
        tempo_bpm=args.finale_tempo,
    )
    pitch = MoviePitch(
        title=args.title,
        antagonist=args.antagonist,
        hook=args.hook,
        finale_song=finale,
    )
    return pitch.synopsis()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create Regular Show inspired songs, fan videos, and movies."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    song_parser = subparsers.add_parser("song", help="Create a vocal arrangement")
    song_parser.add_argument("title", help="Song title")
    song_parser.add_argument("--lead", help="Lead vocalist", choices=list(VOICE_CAST.keys()) + [SYDNEY["name"]])
    song_parser.add_argument(
        "--background",
        nargs="+",
        help="Background vocalists",
        choices=list(VOICE_CAST.keys()) + [SYDNEY["name"]],
    )
    song_parser.add_argument("--vibe", default="retro future funk", help="Song vibe descriptor")
    song_parser.add_argument("--tempo", type=int, default=118, help="Tempo in BPM")
    song_parser.add_argument("--json", action="store_true", help="Output JSON blueprint")
    song_parser.set_defaults(func=build_song)

    fan_parser = subparsers.add_parser("fanvideo", help="Outline a fan-made video")
    fan_parser.add_argument("title", help="Video title")
    fan_parser.add_argument("--theme", default="park friendships", help="Central theme")
    fan_parser.add_argument("--setting", default="The Park at sunset", help="Main setting")
    fan_parser.set_defaults(func=build_fan_video)

    movie_parser = subparsers.add_parser("movie", help="Pitch a movie idea")
    movie_parser.add_argument("title", help="Movie title")
    movie_parser.add_argument("--antagonist", default="The Time Baby", help="Main villain")
    movie_parser.add_argument(
        "--hook",
        default="The crew must stage the ultimate concert to save the park",
        help="Story hook",
    )
    movie_parser.add_argument("--finale-title", default="Cosmic Harmony", help="Finale song title")
    movie_parser.add_argument(
        "--finale-lead",
        choices=list(VOICE_CAST.keys()) + [SYDNEY["name"]],
        help="Finale lead vocalist",
    )
    movie_parser.add_argument(
        "--finale-background",
        nargs="+",
        choices=list(VOICE_CAST.keys()) + [SYDNEY["name"]],
        help="Finale background vocalists",
    )
    movie_parser.add_argument("--finale-vibe", default="galactic power ballad", help="Finale vibe")
    movie_parser.add_argument("--finale-tempo", type=int, default=105, help="Finale tempo in BPM")
    movie_parser.set_defaults(func=build_movie)

    return parser


def main(argv: List[str] | None = None) -> str:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    print(main())
