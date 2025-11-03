"""Story utilities describing the babysitting adventure."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .characters import Character, default_characters


@dataclass
class Scene:
    """Represents a moment in the mini-movie."""

    title: str
    description: str
    characters: List[Character]

    def summarize(self) -> str:
        cast = ", ".join(character.name for character in self.characters)
        return f"{self.title}\nCast: {cast}\n{self.description}"


def babysitting_story() -> List[Scene]:
    """Construct the canonical story requested by the user."""

    sydney, janie, emily, mordecai, rigby = default_characters()[:5]

    return [
        Scene(
            title="Sydney's Pitch",
            description=(
                "Sydney, with her orange hair and green eyes gleaming, asks Janie to babysit "
                "her daughter Emily Rose so she can direct a new park commercial."
            ),
            characters=[sydney, janie, emily],
        ),
        Scene(
            title="Babysitting Prep",
            description=(
                "Janie assembles her babysitting-ready outfit and packs creative supplies "
                "while Mordecai and Rigby test voice lines for the production booth."
            ),
            characters=[janie, mordecai, rigby],
        ),
        Scene(
            title="Emily's Adventure",
            description=(
                "Emily Rose leads an imagination quest through the park, trying on outfits and "
                "recording adorable voice clips for Sydney's movie maker."
            ),
            characters=[emily, rigby],
        ),
        Scene(
            title="Director's Return",
            description=(
                "Sydney wraps filming with the Regular Show voice cast and returns to find Emily and "
                "Janie editing their footage together in the video generator studio."
            ),
            characters=[sydney, janie, emily, mordecai],
        ),
    ]
