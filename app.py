from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# Разрешаем фронтенду обращаться к бэкенду
CORS(app)

# Ваш API ключ остается в безопасности на сервере
API_KEY = 'deb9d466-c73d-495c-9c97-69b56360cff5'

@app.route('/api/places', methods=['GET'])
def get_places():
    query = request.args.get('q', 'ресторан Астана')
    page = request.args.get('page', 1)
    
    url = "https://catalog.api.2gis.com/3.0/items"
    params = {
        'q': query,
        'key': API_KEY,
        'fields': 'items.point,items.address,items.rubrics',
        'type': 'branch',
        'page': page,
        'page_size': 10,
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
    # Эти данные теперь приходят с сервера
    events = [
        {
            "id": 1,
            "title": "Фестиваль национальной кухни",
            "date": "20-22 февраля 2026",
            "location": "Хан Шатыр",
            "description": "Дегустация блюд разных народов Астаны"
        },
        {
            "id": 2,
            "title": "Концерт 'Ночь в опере'",
            "date": "25 февраля 2026",
            "location": "Театр оперы и балета",
            "description": "Лучшая классическая музыка для жителей столицы"
        }
    ]
    return jsonify(events)

if __name__ == '__main__':
    print("🚀 Сервер запущен на http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
