from pymongo import MongoClient, database, errors
from pymongo.server_api import ServerApi


def get_all(db: database.Database):
    """Виводить усі записи з колекції.

    Аргументи:
        db (database.Database): Об'єкт бази даних.

    Повертає:
        list[str]: Список усіх наявних записів.

    Підіймає:
        ConnectionError: Якщо не вдається підключитися до бази даних.
        TimeoutError: Якщо запит до сервера перевищив час очікування.
        AttributeError: Якщо колекція не існує.
    """
    res = db.cats.find({})
    return [el for el in res]


def get_cat(db: database.Database, name):
    """Виводить запис кота за іменем.

    Аргументи:
        db (database.Database): Об'єкт бази даних.
        name (str): Ім'я кота.

    Повертає:
        str, None: Запис з інформацією про кота або None, якщо кота не існує.

    Підіймає:
        ConnectionError: Якщо не вдається підключитися до бази даних.
        TimeoutError: Якщо запит до сервера перевищив час очікування.
        AttributeError: Якщо колекція не існує.
    """
    try:
        return db.cats.find_one({"name": name})
        
    except errors.ConnectionFailure:
        raise ConnectionError("Failed to connect to the database.")
    
    except errors.ServerSelectionTimeoutError:
        raise TimeoutError("Server selection timed out. Could not reach the database.")
    
    except AttributeError:
        raise ValueError("Invalid database or collection.")


def update_age(db: database.Database, name, new_age):
    """Оновлює вік кота за іменем.

    Аргументи:
        db (database.Database): Об'єкт бази даних.
        name (str): Ім'я кота.
        new_age (int): Новий вік.

    Повертає:
        str: Результат операції.

    Підіймає:
        ConnectionError: Якщо не вдається підключитися до бази даних.
        TimeoutError: Якщо запит до сервера перевищив час очікування.
        AttributeError: Якщо колекція не існує.
    """
    
    try:
        res = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
        return f"{name}'s age update." if res.matched_count == 1 else "No such cat."
    
    except errors.ConnectionFailure:
        raise ConnectionError("Failed to connect to the database.")
    
    except errors.ServerSelectionTimeoutError:
        raise TimeoutError("Server selection timed out. Could not reach the database.")
    
    except AttributeError:
        raise ValueError("Invalid database or collection.")


def add_feature(db: database.Database, name, new_feature):
    """Додає характеристику коту за іменем.

    Аргументи:
        db (database.Database): Об'єкт бази даних.
        name (str): Ім'я кота.
        new_feature (int): Нова характеристика.

    Повертає:
        str: Результат операції.

    Підіймає:
        ConnectionError: Якщо не вдається підключитися до бази даних.
        TimeoutError: Якщо запит до сервера перевищив час очікування.
        AttributeError: Якщо колекція не існує.
    """
    
    try:
        res = db.cats.update_one({"name": name}, {"$addToSet": {"features": new_feature}})
        return f"{name}'s feature added." if res.matched_count == 1 else "No such cat."
    
    except errors.ConnectionFailure:
        raise ConnectionError("Failed to connect to the database.")
    
    except errors.ServerSelectionTimeoutError:
        raise TimeoutError("Server selection timed out. Could not reach the database.")
    
    except AttributeError:
        raise ValueError("Invalid database or collection.")


def del_cat(db: database.Database, name):
    """Видаляє кота за іменем.

    Аргументи:
        db (database.Database): Об'єкт бази даних.
        name (str): Ім'я кота.

    Повертає:
        str: Результат операції.

    Підіймає:
        ConnectionError: Якщо не вдається підключитися до бази даних.
        TimeoutError: Якщо запит до сервера перевищив час очікування.
        AttributeError: Якщо колекція не існує.
    """

    try:
        res = db.cats.delete_one({"name": name})
        return f'{name} deleted.' if res.deleted_count == 1 else 'No such cat.'
    
    except errors.ConnectionFailure:
        raise ConnectionError("Failed to connect to the database.")
    
    except errors.ServerSelectionTimeoutError:
        raise TimeoutError("Server selection timed out. Could not reach the database.")
    
    except AttributeError:
        raise ValueError("Invalid database or collection.")


def del_all(db: database.Database):
    """Видаляє всі записи.

    Аргументи:
        db (database.Database): Об'єкт бази даних.

    Повертає:
        str: Результат операції.

    Підіймає:
        ConnectionError: Якщо не вдається підключитися до бази даних.
        TimeoutError: Якщо запит до сервера перевищив час очікування.
        AttributeError: Якщо колекція не існує.
    """

    try:
        res = db.cats.delete_many({})
        return 'All cats deleted.' if res.deleted_count > 0 else 'Collection already empty.'
    
    except errors.ConnectionFailure:
        raise ConnectionError("Failed to connect to the database.")
    
    except errors.ServerSelectionTimeoutError:
        raise TimeoutError("Server selection timed out. Could not reach the database.")
    
    except AttributeError:
        raise ValueError("Invalid database or collection.")

