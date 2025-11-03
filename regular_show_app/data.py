"""Data helpers for Regular Show fan content generation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Character:
    """Representation of a Regular Show character."""

    name: str
    traits: List[str]
    catchphrase: str | None = None


CHARACTERS: List[Character] = [
    Character(
        name="Mordecai",
        traits=["blue jay", "laid-back", "artistic", "gamer"],
        catchphrase="Dude, we're so busted!",
    ),
    Character(
        name="Rigby",
        traits=["raccoon", "impulsive", "hyper", "loyal"],
        catchphrase="Stop talking!",
    ),
    Character(
        name="Benson",
        traits=["gumball machine", "manager", "no-nonsense"],
        catchphrase="You're fired!",
    ),
    Character(
        name="Skips",
        traits=["immortal", "wise", "yeti", "mystic"],
        catchphrase="I've seen this before.",
    ),
    Character(
        name="Pops",
        traits=["naïve", "joyful", "lollipop person"],
        catchphrase="Good show!",
    ),
    Character(
        name="Muscle Man",
        traits=["green", "prankster", "strong"],
        catchphrase="My mom!",
    ),
    Character(
        name="Hi-Five Ghost",
        traits=["transparent", "chill", "supportive"],
    ),
    Character(
        name="Eileen",
        traits=["smart", "kind", "intern"],
    ),
    Character(
        name="CJ",
        traits=["cloud", "adventurous", "tough"],
    ),
]


LOCATIONS = [
    "the park",
    "the house",
    "the coffee shop",
    "the arcade",
    "the Moon",  # Episode "The Power"
    "Skips' garage",
    "the Dome",
    "Death's realm",
]


PROPS = [
    "magic keyboard",
    "portal to another dimension",
    "retro arcade cabinet",
    "haunted VHS tape",
    "giant sandwich",
    "galactic skateboard",
    "karaoke machine",
    "enchanted VHS camera",
]
