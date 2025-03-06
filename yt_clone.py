from flask import Flask, render_template_string, request
import requests


app = Flask(__name__)

# Replace 'YOUR_YOUTUBE_API_KEY' with your actual YouTube Data API key
YOUTUBE_API_KEY = 'AIzaSyA2G1Gnhf54ty97f5d-nZvyy_Q7Hq_Auf8'  # Replace with your actual key
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

@app.route('/', methods=['GET', 'POST'])
def index():
    videos = []
    if request.method == 'POST':
        query = request.form['query']
        response = requests.get(YOUTUBE_API_URL, params={
            'part': 'snippet',
            'q': query,
            'type': 'video',
            'key': YOUTUBE_API_KEY,
            'maxResults': 5
        })
        data = response.json()
        videos = data.get('items', [])
    return render_template_string(INDEX_HTML, videos=videos)

# HTML template as a string variable with a red and black color scheme
INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Clone</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #000000; /* Black background */
            color: #FFFFFF; /* White text color */
            margin: 0;
            padding: 0;
            min-height: 100vh;
        }
        h1 {
            margin-top: 20px;
            color: #FF0000; /* Red color for the main heading */
        }
        form {
            margin: 20px 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        input[type="text"] {
            padding: 10px;
            width: 300px;
            margin-bottom: 10px;
            border: 1px solid #FF0000; /* Red border for input */
            border-radius: 4px;
            background-color: #1A1A1A; /* Darker background for input */
            color: #FFFFFF; /* White text color for input */
        }
        button {
            padding: 10px 20px;
            background-color: #FF0000; /* Red button background */
            color: #FFFFFF; /* White text color for button */
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #CC0000; /* Darker red on hover */
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 20px;
            border-bottom: 1px solid #FF0000; /* Red border for video items */
            padding-bottom: 10px;
        }
        iframe {
            border: none;
        }
    </style>
</head>
<body>
    <h1>YouTube Clone</h1>
    <form method="POST">
        <input type="text" name="query" placeholder="Search for videos..." required>
        <button type="submit">Search</button>
    </form>
    <ul>
        {% for video in videos %}
            <li>
                <h3>{{ video.snippet.title }}</h3>
                <iframe width="560" height="315" 
                        src="https://www.youtube.com/embed/{{ video.id.videoId }}" 
                        frameborder="0" 
                        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
                        allowfullscreen>
                </iframe>
                <p>{{ video.snippet.description }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)