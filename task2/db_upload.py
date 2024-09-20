from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json

client = MongoClient(
    "mongodb+srv://alexeroalex:7CuqApF42x58y8QR@cluster0.ejpi7.mongodb.net/",
    server_api=ServerApi('1')
)

db = client.quote_scraping

# Читання з json файлів
with open('quotes.json', 'r') as file:
    data_quotes = json.load(file)

with open('authors.json', 'r') as file:
    data_authors = json.load(file)

# Додавання записів до відповідниз колекцій в БД
db.quotes.insert_many(data_quotes)
db.authors.insert_many(data_authors)