from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app) # Enable CORS for frontend communication

# Get your key at platform.2gis.ru
# Replace the default string with your actual key in the .env file
API_KEY = os.getenv('DG_API_KEY', 'deb9d466-c73d-495c-9c97-69b56360cff5')

@app.route('/api/places', methods=['GET'])
def get_places():
    query = request.args.get('q', 'ресторан Астана')
    page = request.args.get('page', 1)
    page_size = request.args.get('page_size', 10)
    
    url = "https://catalog.api.2gis.com/3.0/items"
    params = {
        'q': query,
        'key': API_KEY,
        'fields': 'items.point,items.address,items.rubrics',
        'type': 'branch',
        'page': page,
        'page_size': page_size,
        'sort': 'relevance',
        'locale': 'ru_RU'
    }
    
    try:
        response = requests.get(url, params=params)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"meta": {"code": 500, "error": {"message": str(e)}}}), 500

@app.route('/api/events', methods=['GET'])
def get_events():
    # This can be expanded to pull from a database later
    events = [
        {
            "id": 1,
            "title": "Фестиваль национальной кухни",
            "date": "20-22 февраля 2026",
            "location": "Хан Шатыр",
            "description": "Дегустация блюд разных народов"
        },
        {
            "id": 2,
            "title": "Концерт \"Ночь в опере\"",
            "date": "25 февраля 2026",
            "location": "Театр оперы и балета",
            "description": "Классическая музыка"
        }
    ]
    return jsonify(events)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
