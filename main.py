import yaml
from jinja2 import Template
import os

# Read YAML file
with open("playlist.yml", "r") as file:
    playlists = yaml.safe_load(file)

# HTML Template for the page
template = Template('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SilverBass - Weekly Playlist</title>
</head>
<body>
    <h1>Weekly Music Playlist</h1>
    {% for playlist in playlists %}
        <h2>{{ playlist.theme }}</h2>
        <ul>
        {% for song in playlist.songs %}
            <li>{{ song.title }} by {{ song.artist }} - <a href="{{ song.url }}">Listen</a></li>
        {% endfor %}
        </ul>
    {% endfor %}
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
