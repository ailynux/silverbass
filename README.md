<div align="center">

# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Headphone.png" alt="Headphone" width="60" height="60" /> SilverBass <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Speaker%20High%20Volume.png" alt="Speaker" width="60" height="60" />

### A weekly, hand-picked music playlist — with a built-in player. Press play. 🎧

![Python](https://img.shields.io/badge/Built%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jinja](https://img.shields.io/badge/Templated%20with-Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![YAML](https://img.shields.io/badge/Data-YAML-F3C613?style=for-the-badge&logo=yaml&logoColor=white)
![Docker](https://img.shields.io/badge/Containerized-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/Live%20on-GitHub%20Pages-222?style=for-the-badge&logo=github)

**[▶ Open the live site](https://ailynux.github.io/silverbass/)**

</div>

---

SilverBass turns a simple `playlist.yml` file into a **gorgeous, fully-interactive music site**. Add a song's title, artist, and YouTube link — the generator does the rest: it pulls the cover art, builds the cards, and wires up a real player. No frontend code required to update your music.

<div align="center">
    <img src="images/preview-hero.png" alt="SilverBass preview" width="760" />
</div>

---

## ✨ What it does

- **🎛️ Built-in player** — click any track and a sticky "Now Playing" bar slides up with play/pause, previous/next, **shuffle**, **repeat**, autoplay-next, a scrubber, and a live **audio visualizer**. Powered by the YouTube IFrame API.
- **🖼️ Automatic cover art** — album/video thumbnails are pulled straight from each YouTube link. Just paste a URL.
- **❤️ Likes that stick** — heart any track and it's saved in your browser, with a dedicated "Liked" filter.
- **🔗 Shareable deep-links** — the Share button copies a link that opens the site *already cued to that song* (native share sheet on mobile).
- **🔎 Live search & genre chips** — filter every song/artist as you type, or jump between playlists instantly.
- **🐟 Underwater easter eggs** — a school of 3D silverbass swim by, bubbles drift up, and clicking a fish starts a "feeding frenzy".
- **⌨️ Keyboard shortcuts** — `space`, `←/→`, `s`, `r`, `l` like, `c` copy link, `/` search, `?` help.
- **💎 Premium UI** — animated aurora background, glassmorphism cards, per-playlist accent colors, fully responsive.
- **🤖 Hands-off updates** — GitHub Actions rebuilds and redeploys the site on every push (and weekly).

---

## 🧱 How it works

```
playlist.yml  ──►  main.py (Jinja2)  ──►  docs/index.html  ──►  GitHub Pages
   your music        generator            the website          the internet
```

| Tech | Role |
| --- | --- |
| 🐍 **Python** | Reads the YAML, extracts YouTube IDs + cover art, renders the page |
| 🧩 **Jinja2** | `templates/index.html.j2` — the page template |
| 📑 **YAML** | `playlist.yml` — your single source of truth for songs |
| 🎮 **Vanilla JS** | The player, search, and filters (no frameworks) |
| 🐋 **Docker** | Reproducible build environment |
| 🔧 **GitHub Actions** | Weekly + on-push build & deploy |
| 🌐 **GitHub Pages** | Hosting |

---

## 🚀 Quick start

```bash
# 1. Clone
git clone https://github.com/ailynux/silverbass.git
cd silverbass

# 2. Install + build (Python)
pip install -r requirements.txt
python main.py

# 3. Preview
open docs/index.html
```

Prefer Docker?

```bash
docker build -t silverbass .
docker run --rm -v "$PWD/docs:/app/docs" silverbass
```

---

## 🎵 Adding songs

Edit `playlist.yml` — that's the only file you touch:

```yaml
playlists:
  - theme: "Chill Vibes"
    emoji: "🌙"
    genre: "Indie / Dream"
    accent: "#7c5cff"      # optional accent color for this set
    songs:
      - title: "Space Song"
        artist: "Beach House"
        url: "https://www.youtube.com/watch?v=RBtlPT23PTM"
```

Run `python main.py` (or just push — Actions handles it) and the new track shows up with cover art and full playback. ✨

---

## 🎉 Connect

- 💻 [GitHub](https://github.com/ailynux)
- 👔 [LinkedIn](https://www.linkedin.com/in/ailyndiaz01)

<div align="center">

⭐ Star the repo if SilverBass made your week sound better.

[![Typing SVG](https://readme-typing-svg.demolab.com/?lines=Thanks+for+stopping+by!;Press+play+and+enjoy.;Star+the+repo+if+you+liked+it!)](https://git.io/typing-svg)

</div>
