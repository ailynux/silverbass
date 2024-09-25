#main.py

import yaml
from jinja2 import Template
import os

# Read YAML file
with open("playlist.yml", "r") as file:
    playlists = yaml.safe_load(file)

# HTML 
template = Template('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SilverBass</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
         body {
            font-family: 'Roboto', sans-serif;
            background-color: #121212;
            color: #e0e0e0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }


       h1 {
            font-size: 3rem;
            font-weight: 700;
            color: #fff;
            background-color: #1f1f1f;
            padding: 40px 20px;
            border-radius: 10px;
            position: relative;
            overflow: hidden;
            margin-bottom: 40px;
            box-shadow: 0 0 10px #ffcc00, 0 0 20px #ff6f61, 0 0 30px #1db954, 0 0 40px #ff6f61;
            animation: glowPulse 3s ease-in-out infinite; /* Glowing pulse animation */
            display: inline-block;
            text-align: center;
        }

        h1::before {
            content: "🎣";
            font-size: 1.5rem;
            position: absolute;
            left: -30px;
            top: 50%;
            transform: translateY(-50%);
            animation: fishSwim 5s ease-in-out infinite;
        }

        h1 .badges {
            display: block;
            margin-top: 10px;
        }

        h1 img {
            margin: 0 5px;
            vertical-align: middle;
            transition: transform 0.2s ease;
        }

        h1 img:hover {
            transform: scale(1.2);
        }

        @keyframes glowPulse {
            0% {
                box-shadow: 0 0 10px #ffcc00, 0 0 20px #ff6f61, 0 0 30px #1db954, 0 0 40px #ff6f61;
                color: #fff;
            }
            50% {
                box-shadow: 0 0 20px #1db954, 0 0 30px #ffcc00, 0 0 40px #ff6f61, 0 0 50px #ffcc00;
                color: #ffcc00;
            }
            100% {
                box-shadow: 0 0 10px #ffcc00, 0 0 20px #ff6f61, 0 0 30px #1db954, 0 0 40px #ff6f61;
                color: #fff;
            }
        }

        @keyframes fishSwim {
            0%, 100% { left: -30px; }
            50% { left: 100%; }
        }

        h2 {
            font-size: 1.75rem;
            color: #ff6f61;
            margin: 30px 0 10px 0;
            border-bottom: 1px solid #333;
            padding-bottom: 10px;
        }
        ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }
        li {
            background-color: #1f1f1f;
            margin: 10px 0;
            padding: 20px;
            border-radius: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }
        li:hover {
            background-color: #2a2a2a;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.5);
        }
        a {
            color: #1db954;
            text-decoration: none;
            font-weight: 500;
        }
        a:hover {
            color: #1ed760;
        }
        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            background-color: #121212;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
            border-radius: 15px;
        }
        footer {
            text-align: center;
            padding: 20px;
            font-size: 0.9rem;
            color: #aaa;
        }
    </style>
</head>
<body>
   <h1>
    🎣 SilverBass - Weekly Music Playlist
    <span class="badges">
        <img src="https://img.shields.io/badge/Music-Spotify-%231DB954?style=flat-square&logo=spotify&logoColor=white" alt="Spotify Badge">
        <img src="https://img.shields.io/badge/Playlist-Updated%20Weekly-blue?style=flat-square" alt="Weekly Playlist Badge">
        <img src="https://img.shields.io/badge/Genre-Variety-orange?style=flat-square" alt="Genre Variety Badge">
    </span>
</h1>
    <div class="container">
    {% for playlist in playlists %}
        <h2>{{ playlist.theme }}</h2>
        <ul>
        {% for song in playlist.songs %}
            <li>{{ song.title }} by {{ song.artist }} - <a href="{{ song.url }}" target="_blank">Listen</a></li>
        {% endfor %}
        </ul>
    {% endfor %}
    <footer>
        <p>Connect with me on <a href="https://github.com/ailynux" target="_blank">GitHub</a> or <a href="https://www.linkedin.com/in/ailyndiaz01" target="_blank">LinkedIn</a>.</p>
    </footer>
    </div>
</body>
</html>
''')

# Render the HTML
rendered_html = template.render(playlists=playlists['playlists'])

# Save the generated HTML to the docs folder for GitHub Pages
os.makedirs("docs", exist_ok=True)
with open("docs/index.html", "w") as f:
    f.write(rendered_html)

print("SilverBass Playlist page generated.")
