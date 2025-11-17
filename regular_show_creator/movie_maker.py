"""Movie planning helper built around the Regular Show cast."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List

from .cast import CastMember, get_cast


@dataclass
class Act:
    """A movie act comprised of multiple set pieces."""

    title: str
    key_events: List[str]


@dataclass
class MovieMaker:
    """Convenience class for planning feature-length adventures."""

    title: str
    logline: str
    cast: List[CastMember] = field(default_factory=get_cast)
    acts: List[Act] = field(default_factory=list)

    def add_act(self, title: str, key_events: Iterable[str]) -> None:
        """Add an act to the movie outline."""

        self.acts.append(Act(title=title, key_events=list(key_events)))

    def build_outline(self) -> str:
        """Return a formatted outline including acts and casting information."""

        lines = [f"Title: {self.title}", f"Logline: {self.logline}", "Cast:"]
        for member in self.cast:
            lines.append(f"  - {member.character} (voice: {member.voice_actor})")
        if not self.acts:
            lines.append("No acts have been planned yet.")
        else:
            lines.append("Acts:")
            for index, act in enumerate(self.acts, start=1):
                lines.append(f"  {index}. {act.title}")
                for event in act.key_events:
                    lines.append(f"       • {event}")
        return "\n".join(lines)


__all__ = ["Act", "MovieMaker"]
