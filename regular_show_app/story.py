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

    characters = {character.name: character for character in default_characters()}
    sydney = characters["Sydney"]
    janie = characters["Janie"]
    emily = characters["Emily Rose"]
    mordecai = characters["Mordecai"]
    rigby = characters["Rigby"]
    jayla = characters["Jayla"]

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
            title="Jayla's Messy Arrival",
            description=(
                "Jayla stomps into the studio with dirty clothes, scuffed shoes, and a smirk, "
                "teasing Janie until art supplies scatter across the floor."
            ),
            characters=[jayla, janie, rigby],
        ),
        Scene(
            title="Janie Storms Out",
            description=(
                "Embarrassed and upset, Janie drops her satchel, abandons the storyboard, and storms "
                "out for fresh air while Sydney's team scrambles to calm Jayla down."
            ),
            characters=[janie, jayla, mordecai],
        ),
        Scene(
            title="Crew Mediation",
            description=(
                "Mordecai and Rigby coach Jayla through a heartfelt apology, wiping away smudges and "
                "inviting her to help rebuild the toppled set before Janie returns."
            ),
            characters=[jayla, mordecai, rigby],
        ),
        Scene(
            title="Emily's Adventure",
            description=(
                "Emily Rose turns the tension into playtime, guiding Jayla through a calmer craft "
                "session while Janie documents the moment for Sydney's video generator."
            ),
            characters=[emily, jayla, janie],
        ),
        Scene(
            title="Director's Return",
            description=(
                "Sydney wraps filming with the Regular Show voice cast and returns to find Jayla "
                "and Janie editing their footage together in the video generator studio while Emily "
                "cheers them on."
            ),
            characters=[sydney, janie, emily, jayla, mordecai],
        ),
    ]
