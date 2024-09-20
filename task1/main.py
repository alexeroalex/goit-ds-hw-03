from pymongo import MongoClient
from pymongo.server_api import ServerApi
import db_features

client = MongoClient(
    "mongodb+srv://alexeroalex:7CuqApF42x58y8QR@cluster0.ejpi7.mongodb.net/",
    server_api=ServerApi('1')
)

db = client.book

result_one = db.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)

result_many = db.cats.insert_many(
    [
        {
            "name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)

print(db_features.get_all(db))
print(db_features.get_cat(db, 'Liza'))

print(db_features.update_age(db, 'barsik', 7))
print(db_features.add_feature(db, 'barsik', 'чистий'))
print(db_features.get_cat(db, 'barsik'))

print(db_features.del_cat(db, 'Lama'))
print(db_features.get_all(db))
print(db_features.del_all(db))
print(db_features.get_all(db))