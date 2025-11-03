"""Generate fan art, video, and movie ideas for Regular Show."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable, List, Sequence

from .data import CHARACTERS, LOCATIONS, PROPS, Character


@dataclass
class FanArtPrompt:
    """A creative prompt describing a fan art concept."""

    title: str
    description: str
    characters: List[str]


@dataclass
class FanVideoPlan:
    """Outline for a short-form fan video idea."""

    hook: str
    scenes: List[str]
    featured_characters: List[str]


@dataclass
class FanMoviePlot:
    """Story outline for a longer fan film."""

    synopsis: str
    acts: List[str]
    starring: List[str]


def _choose_characters(count: int) -> List[Character]:
    """Return ``count`` unique characters sampled from the roster."""

    if count <= 0:
        raise ValueError("count must be positive")
    if count > len(CHARACTERS):
        raise ValueError("count exceeds available characters")
    selected = random.sample(CHARACTERS, count)
    return list(selected)


def _join(items: Iterable[str]) -> str:
    return ", ".join(items)


def _generate_title(characters: Sequence[Character], medium: str) -> str:
    primary = characters[0]
    if medium == "art":
        return f"{primary.name}'s {random.choice(['Epic', 'Cosmic', 'Radical'])} {random.choice(['Showdown', 'Vibe', 'Portrait'])}"
    if medium == "video":
        return f"{primary.name} & Friends: {random.choice(['Glitch', 'Quest', 'Mixtape'])}"
    return f"{primary.name}: {random.choice(['Chronicles', 'Saga', 'Dimension Drift'])}"


def generate_fan_art_prompt(character_count: int = 2) -> FanArtPrompt:
    """Create a prompt for an illustration featuring Regular Show characters."""

    characters = _choose_characters(character_count)
    location = random.choice(LOCATIONS)
    prop = random.choice(PROPS)
    title = _generate_title(characters, medium="art")
    description = (
        f"Illustrate {_join(c.name for c in characters)} hanging out at {location} while "
        f"experimenting with a {prop}. Capture the show's surreal humor and "
        "vibrant color palette."
    )
    return FanArtPrompt(
        title=title,
        description=description,
        characters=[c.name for c in characters],
    )


def _make_hook(characters: Sequence[Character]) -> str:
    protagonist = characters[0]
    prop = random.choice(PROPS)
    return (
        f"{protagonist.name} discovers a {prop} that sends the park into "
        f"{random.choice(['slow motion', 'a musical montage', '8-bit chaos'])}."
    )


def _make_scenes(characters: Sequence[Character]) -> List[str]:
    supporting = characters[1:]
    beats = [
        f"Cold open: {_join(c.name for c in characters)} slack off before chaos erupts.",
        f"Complication: {_join(c.name for c in supporting) or characters[0].name} tries to fix the mess but only escalates it.",
        f"Climax: Skips arrives with mystical advice that kind of works.",
        "Tag: Benson yells at everyone while Pops applauds the spectacle.",
    ]
    random.shuffle(beats)
    return beats


def generate_fan_video_plan(character_count: int = 3) -> FanVideoPlan:
    """Generate a short video outline using Regular Show characters."""

    characters = _choose_characters(character_count)
    hook = _make_hook(characters)
    scenes = _make_scenes(characters)
    return FanVideoPlan(
        hook=hook,
        scenes=scenes,
        featured_characters=[c.name for c in characters],
    )


def _make_act(act_number: int, characters: Sequence[Character]) -> str:
    focus = random.choice(characters)
    location = random.choice(LOCATIONS)
    if act_number == 1:
        return (
            f"Act I: {focus.name} accidentally signs the park up for a cosmic talent show at {location},"
            " forcing everyone to train."
        )
    if act_number == 2:
        return (
            f"Act II: {focus.name} discovers the contest is judged by an interdimensional council,"
            " and the team must master bizarre challenges."
        )
    return (
        f"Act III: In the finale at {location}, {_join(c.name for c in characters)} combine their quirks "
        "to out-weird the competition and save the park."
    )


def generate_fan_movie_plot(character_count: int = 4) -> FanMoviePlot:
    """Produce a three-act fan film outline."""

    characters = _choose_characters(character_count)
    synopsis = (
        f"When {_join(c.name for c in characters)} discover a hidden rift beneath the park,"
        " they must team up to stop cosmic boredom from erasing Regular City."
    )
    acts = [_make_act(i, characters) for i in range(1, 4)]
    return FanMoviePlot(
        synopsis=synopsis,
        acts=acts,
        starring=[c.name for c in characters],
    )


__all__ = [
    "FanArtPrompt",
    "FanVideoPlan",
    "FanMoviePlot",
    "generate_fan_art_prompt",
    "generate_fan_video_plan",
    "generate_fan_movie_plot",
]
