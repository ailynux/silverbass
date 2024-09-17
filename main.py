import yaml
from jinja2 import Template
import os

# Read YAML file
with open("playlist.yml", "r") as file:
    playlists = yaml.safe_load(file)

# HTML Template with dark, minimal, and refined CSS styling
template = Template('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SilverBass - Weekly Playlist</title>
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #121212;
            color: #e0e0e0;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            color: #fff;
            text-align: center;
            margin: 0;
            padding: 30px;
            background-color: #1f1f1f;
            border-bottom: 1px solid #333;
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
        /* Scrollbar Styling */
        ::-webkit-scrollbar {
            width: 10px;
        }
        ::-webkit-scrollbar-thumb {
            background-color: #333;
            border-radius: 5px;
        }
        ::-webkit-scrollbar-track {
            background-color: #121212;
        }
    </style>
</head>
<body>
    <h1>SilverBass - Weekly Music Playlist</h1>
    <div class="container">
    {% for playlist in playlists %}
        <h2>{{ playlist.theme }}</h2>
        <ul>
        {% for song in playlist.songs %}
            <li>{{ song.title }} by {{ song.artist }} - <a href="{{ song.url }}" target="_blank">Listen</a></li>
        {% endfor %}
        </ul>
    {% endfor %}
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
