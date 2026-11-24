"""Build one Pages artifact containing the StoryMap, Jupyter Book, and JupyterLite."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BOOK = ROOT / "book"
LAB = ROOT / "lab"


def run(*args: str) -> None:
    print("+", " ".join(args), flush=True)
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    shutil.copytree(ROOT / "storymap", SITE)

    for destination in (BOOK / "data", LAB / "files" / "data"):
        destination.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / "storymap" / "stops.json", destination / "tour-stops.json")

    lab_notebooks = LAB / "files" / "notebooks"
    lab_notebooks.mkdir(parents=True, exist_ok=True)
    for notebook in (BOOK / "notebooks").glob("*.ipynb"):
        shutil.copy2(notebook, lab_notebooks / notebook.name)
    shutil.copy2(LAB / "README.md", LAB / "files" / "README.md")

    run("jupyter-book", "build", "book")
    shutil.copytree(BOOK / "_build" / "html", SITE / "book")

    run(
        "jupyter", "lite", "build", "--disable-addons", "jupyterlite-xeus",
        "--lite-dir", "lab", "--contents", "files",
        "--output-dir", str(SITE / "lab"),
    )

    expected = (
        SITE / "index.html",
        SITE / "book" / "index.html",
        SITE / "lab" / "lab" / "index.html",
        SITE / "lab" / "files" / "notebooks" / "timeline.ipynb",
        SITE / "lab" / "files" / "data" / "tour-stops.json",
    )
    missing = [str(path) for path in expected if not path.exists()]
    if missing:
        raise RuntimeError(f"Site build is incomplete: {missing}")
    print("Built StoryMap, book, and lab in", SITE, flush=True)


if __name__ == "__main__":
    try:
        main()
    except (OSError, subprocess.CalledProcessError, RuntimeError) as exc:
        print(exc, file=sys.stderr)
        raise SystemExit(1) from exc
