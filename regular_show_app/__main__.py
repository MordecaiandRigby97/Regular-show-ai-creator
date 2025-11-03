"""Enable `python -m regular_show_app` to launch the CLI."""
from __future__ import annotations

from .main import run_cli


def main() -> None:
    """Entry point that simply proxies to :func:`run_cli`."""

    run_cli()


if __name__ == "__main__":
    main()
