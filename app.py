from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

# Ваш API ключ
API_KEY = 'deb9d466-c73d-495c-9c97-69b56360cff5'

@app.route('/')
def index():
    # Эта функция откроет ваш index.html, когда вы перейдете на http://127.0.0.1:5000
    return send_from_directory('.', 'index.html')

@app.route('/api/places')
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
        # Если 2GIS вернул не JSON, мы поймаем это здесь
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"meta": {"code": 500, "error": {"message": "Ошибка 2GIS или ключа"}}}), 500

@app.route('/api/events')
def get_events():
    return jsonify([
        {"title": "Фестиваль еды", "date": "20 Фев", "location": "Хан Шатыр", "description": "Вкусная еда"},
        {"title": "Концерт", "date": "25 Фев", "location": "Астана Опера", "description": "Классическая музыка"}
    ])

if __name__ == '__main__':
    print("------------------------------------------")
    print("🚀 САЙТ ЗАПУЩЕН!")
    print("👉 Перейдите по ссылке: http://127.0.0.1:5000")
    print("------------------------------------------")
    app.run(debug=True, port=5000)
