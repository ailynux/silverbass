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
            flex-direction: row; /* Stacks elements in a column */
            align-items: center; /* Centers the content */
            min-height: 100vh;
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
            margin-bottom: 40px;
            box-shadow: 0 0 10px #ffcc00, 0 0 20px #ff6f61, 0 0 30px #1db954, 0 0 40px #ff6f61;
            animation: glowPulse 3s ease-in-out infinite;
            display: inline-block;
            max-width: 90%; /* Ensure it fits within smaller screens */
            margin-left: 30px; /* Ensure it fits within smaller screens */
        }

        h1::before {
            content: "🐟";
            font-size: 1.5rem;
            position: absolute;
            left: -30px;
            top: 50%;
            transform: translateY(-50%);
            animation: fishSwim 9s ease-in-out infinite;
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
            width: 100%; /* Takes full width on smaller screens */
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

        /* Media query for tablet responsiveness (max-width: 768px) */
        @media (max-width: 768px) {
            body {
            flex-direction: column; /* Stacks elements in a column */
            }

            h1 {
                font-size: 2rem;
                padding: 20px;
                margin-bottom: 20px;
                max-width: 100%; /* Make sure the header fits */
                margin-right: 30px; /* Ensure it fits within smaller screens */
            }

            .container {
                width: 95%; /* Fit within the screen */
                padding: 15px;
                margin: 20px auto;
            }

            ul {
                padding: 0;
                margin: 0;
            }

            li {
                padding: 15px;
                font-size: 1rem;
            }
        }

        /* Media query for mobile phones (max-width: 480px) */
        @media (max-width: 480px) {
            h1 {
                font-size: 1.5rem;
                padding: 10px;
                margin-bottom: 15px;
            }

            .container {
                padding: 10px;
                margin: 10px auto;
            }

            li {
                padding: 10px;
                font-size: 0.875rem;
            }
        }
        /* General playlist container styling */
    .playlist-container {
        background-color: #1a1a1a;
        border: 2px solid #ffcc00;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 25px rgba(255, 204, 0, 0.7), 0 0 50px rgba(0, 255, 255, 0.5);
        max-width: 800px;
        margin: 20px auto;
        text-align: left;
        position: relative;
        animation: glowEffect 5s ease-in-out infinite;
    }

    /* Glowing hover effect for the container */
    @keyframes glowEffect {
        0% {
            box-shadow: 0 0 25px rgba(255, 204, 0, 0.7), 0 0 50px rgba(0, 255, 255, 0.5);
        }
        50% {
            box-shadow: 0 0 40px rgba(0, 255, 255, 0.7), 0 0 80px rgba(255, 204, 0, 0.5);
        }
        100% {
            box-shadow: 0 0 25px rgba(255, 204, 0, 0.7), 0 0 50px rgba(0, 255, 255, 0.5);
        }
    }

    /* Playlist titles */
    .playlist-title {
        font-size: 2rem;
        color: #ff6f61;
        background-color: #333;
        padding: 10px 15px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(255, 111, 97, 0.8);
        text-transform: uppercase;
        margin-top: 20px;
        position: relative;
        overflow: hidden;
    }

    /* Adding cool underline animation to the title */
    .playlist-title::after {
        content: '';
        position: absolute;
        left: 0;
        bottom: 0;
        height: 3px;
        width: 100%;
        background-color: #ff6f61;
        animation: underlineEffect 3s ease-in-out infinite;
    }

    @keyframes underlineEffect {
        0% {
            width: 0;
        }
        50% {
            width: 100%;
        }
        100% {
            width: 0;
        }
    }

    /* Playlist items */
    .playlist-list {
        padding-left: 20px;
        margin-top: 10px;
    }

    .playlist-item {
        background-color: #1f1f1f;
        margin: 10px 0;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(29, 185, 84, 0.5);
        font-size: 1.1rem;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }

    .playlist-item:hover {
        background-color: #2a2a2a;
        box-shadow: 0 0 20px rgba(29, 185, 84, 0.7);
    }

    /* Playlist links */
    .playlist-link {
        color: #1db954;
        text-decoration: none;
        font-weight: 600;
        position: relative;
        transition: color 0.3s ease;
    }

    .playlist-link:hover {
        color: #1ed760;
        text-shadow: 0 0 8px rgba(29, 185, 84, 0.8);
    }

    /* Footer styling */
    .playlist-footer {
        margin-top: 30px;
        text-align: center;
        font-size: 1rem;
        color: #aaa;
        border-top: 1px solid #444;
        padding-top: 15px;
    }

    .footer-link {
        color: #ffcc00;
        text-decoration: none;
        position: relative;
        transition: color 0.3s ease;
    }

    .footer-link:hover {
        color: #fff;
        text-shadow: 0 0 10px #ffcc00;
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
<div class="playlist-container">
    {% for playlist in playlists %}
        <h2 class="playlist-title">{{ playlist.theme }}</h2>
        <ul class="playlist-list">
            {% for song in playlist.songs %}
                <li class="playlist-item">{{ song.title }} by {{ song.artist }} - <a href="{{ song.url }}" target="_blank" class="playlist-link">Listen</a></li>
            {% endfor %}
        </ul>
    {% endfor %}
    <footer class="playlist-footer">
        <p>Connect with me on <a href="https://github.com/ailynux" target="_blank" class="footer-link">GitHub</a> or <a href="https://www.linkedin.com/in/ailyndiaz01" target="_blank" class="footer-link">LinkedIn</a>.</p>
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
