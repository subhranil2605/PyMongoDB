from pymongo.collection import Collection
from pymongo import MongoClient
from pymongo.results import InsertOneResult, InsertManyResult


def check_database_exists(client_: MongoClient, db_name: str) -> bool:
    """
    Checks if the database is already exists

    :param client_: MongoClient object
    :param db_name: database name
    :return: str
    """
    all_dbs: list[str] = client_.list_database_names()
    return db_name in all_dbs


def insert(col: Collection, data: dict | list[dict]) -> InsertOneResult | InsertManyResult:
    """
    Insert data into the collection
    :param col: collection
    :param data: document or list of documents
    :return: InsertOneResult or InsertManyResult
    """
    if isinstance(data, dict):
        return col.insert_one(data)
    elif isinstance(data, list):
        return col.insert_many(data)


def print_all_documents(collection: Collection) -> None:
    """
    show all the document in a given collection
    :param collection: Collection object
    """
    [print(col) for col in collection.find()]
