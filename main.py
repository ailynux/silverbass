"""SilverBass static site generator.

Reads playlist.yml, enriches each track with its YouTube id + cover art, and
renders templates/index.html.j2 into docs/index.html for GitHub Pages.
"""

from __future__ import annotations

import os
import re
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlparse

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(ROOT, "playlist.yml")
TEMPLATE_DIR = os.path.join(ROOT, "templates")
OUTPUT_DIR = os.path.join(ROOT, "docs")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "index.html")

DEFAULT_ACCENTS = ["#7c5cff", "#ff5c8a", "#22c98b", "#ffba49", "#3bc9ff", "#ff6f61"]


def youtube_id(url: str) -> str | None:
    """Pull the 11-char video id out of any common YouTube URL shape."""
    if not url:
        return None
    parsed = urlparse(url)
    host = (parsed.hostname or "").replace("www.", "")

    if host == "youtu.be":
        return parsed.path.lstrip("/").split("/")[0] or None
    if host.endswith("youtube.com"):
        if parsed.path == "/watch":
            vid = parse_qs(parsed.query).get("v", [None])[0]
            if vid:
                return vid
        match = re.search(r"/(?:embed|shorts|v)/([A-Za-z0-9_-]{11})", parsed.path)
        if match:
            return match.group(1)

    match = re.search(r"([A-Za-z0-9_-]{11})", url)
    return match.group(1) if match else None


def build_track(song: dict) -> dict:
    """Normalize a raw song dict into something the template can render."""
    url = song.get("url", "")
    vid = youtube_id(url)
    cover = song.get("cover")
    if not cover and vid:
        cover = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
    return {
        "title": song.get("title", "Untitled"),
        "artist": song.get("artist", "Unknown artist"),
        "url": url,
        "video_id": vid,
        "cover": cover,
    }


def build_context(data: dict) -> dict:
    meta = data.get("meta", {}) or {}
    playlists = []
    total = 0
    flat = []

    for i, raw in enumerate(data.get("playlists", []) or []):
        tracks = [build_track(s) for s in raw.get("songs", []) or []]
        total += len(tracks)
        accent = raw.get("accent") or DEFAULT_ACCENTS[i % len(DEFAULT_ACCENTS)]
        slug = re.sub(r"[^a-z0-9]+", "-", raw.get("theme", f"set-{i}").lower()).strip("-")
        playlists.append(
            {
                "theme": raw.get("theme", f"Playlist {i + 1}"),
                "slug": slug,
                "emoji": raw.get("emoji", "🎵"),
                "genre": raw.get("genre", ""),
                "accent": accent,
                "tracks": tracks,
            }
        )
        for t in tracks:
            flat.append({**t, "theme": raw.get("theme", ""), "accent": accent})

    return {
        "meta": {
            "title": meta.get("title", "SilverBass"),
            "tagline": meta.get("tagline", "Weekly music, hand-picked."),
            "curator": meta.get("curator", ""),
            "github": meta.get("github", "https://github.com/ailynux"),
            "linkedin": meta.get("linkedin", ""),
        },
        "playlists": playlists,
        "queue": flat,
        "total_tracks": total,
        "total_sets": len(playlists),
        "updated": datetime.now(timezone.utc).strftime("%B %d, %Y"),
    }


def main() -> None:
    with open(DATA_FILE, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("index.html.j2")
    html = template.render(**build_context(data))

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(html)

    print(f"SilverBass generated -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
