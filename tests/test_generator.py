"""Unit tests for Regular Show fan content generators."""

from __future__ import annotations

import pytest

from regular_show_app import (
    FanArtPrompt,
    FanMoviePlot,
    FanVideoPlan,
    generate_fan_art_prompt,
    generate_fan_movie_plot,
    generate_fan_video_plan,
)


@pytest.mark.parametrize("count", [1, 2, 3])
def test_generate_fan_art_prompt_returns_prompt(count: int) -> None:
    prompt = generate_fan_art_prompt(count)
    assert isinstance(prompt, FanArtPrompt)
    assert len(prompt.characters) == count
    assert prompt.title
    assert "Illustrate" in prompt.description


@pytest.mark.parametrize("count", [2, 3, 4])
def test_generate_fan_video_plan_returns_plan(count: int) -> None:
    plan = generate_fan_video_plan(count)
    assert isinstance(plan, FanVideoPlan)
    assert len(plan.featured_characters) == count
    assert plan.hook
    assert len(plan.scenes) == 4


@pytest.mark.parametrize("count", [3, 4, 5])
def test_generate_fan_movie_plot_returns_plot(count: int) -> None:
    plot = generate_fan_movie_plot(count)
    assert isinstance(plot, FanMoviePlot)
    assert len(plot.starring) == count
    assert plot.synopsis.startswith("When")
    assert len(plot.acts) == 3


def test_invalid_character_counts_raise_value_error() -> None:
    with pytest.raises(ValueError):
        generate_fan_art_prompt(0)
    with pytest.raises(ValueError):
        generate_fan_video_plan(100)
