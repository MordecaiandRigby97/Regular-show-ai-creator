"""Cast utilities for Regular Show inspired productions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class CastMember:
    """Represents a pairing between a character and their voice actor."""

    character: str
    voice_actor: str
    description: str


_REGULAR_SHOW_CAST: List[CastMember] = [
    CastMember(
        character="Mordecai",
        voice_actor="J.G. Quintel",
        description="A blue jay with a laid-back attitude and artistic ambitions.",
    ),
    CastMember(
        character="Rigby",
        voice_actor="William Salyers",
        description="A hyperactive raccoon whose impulsive ideas drive the chaos.",
    ),
    CastMember(
        character="Benson",
        voice_actor="Sam Marin",
        description="The gumball machine manager constantly exasperated by his crew.",
    ),
    CastMember(
        character="Skips",
        voice_actor="Mark Hamill",
        description="An immortal yeti and the voice of reason.",
    ),
    CastMember(
        character="Muscle Man",
        voice_actor="Sam Marin",
        description="A prank-loving groundskeeper obsessed with his own jokes.",
    ),
    CastMember(
        character="High Five Ghost",
        voice_actor="J.G. Quintel",
        description="A literal ghost with a floating hand as his best friend.",
    ),
    CastMember(
        character="Pops",
        voice_actor="Sam Marin",
        description="A lollipop-headed optimist discovering the world with childlike wonder.",
    ),
    CastMember(
        character="Sydney Jayla",
        voice_actor="Linda Cardellini",
        description=(
            "A quick-witted sound engineer who keeps the park's media projects on track."
        ),
    ),
    CastMember(
        character="Emily Rose",
        voice_actor="Courtenay Taylor",
        description=(
            "Sydney Jayla's adventurous sister who documents every wild escapade on film."
        ),
    ),
    CastMember(
        character="Jaylan",
        voice_actor="Minty Lewis",
        description=(
            "Sydney Jayla's imaginative daughter whose story ideas inspire the crew."
        ),
    ),
]


def get_cast(extra_members: Iterable[CastMember] | None = None) -> List[CastMember]:
    """Return the complete cast list including any additional members.

    Parameters
    ----------
    extra_members:
        Optional iterable of additional :class:`CastMember` entries to append to the
        baseline roster.

    Returns
    -------
    list of CastMember
        The combined cast roster preserving insertion order.
    """

    cast = list(_REGULAR_SHOW_CAST)
    if extra_members:
        cast.extend(extra_members)
    return cast


__all__ = ["CastMember", "get_cast"]
