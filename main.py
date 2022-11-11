from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")


def print_all_documents(collection: Collection) -> None:
    """
    show all the document in a given collection
    :param collection: Collection object
    :return: None
    """
    [print(col) for col in collection.find()]


if __name__ == '__main__':
    client: MongoClient = MongoClient('localhost', 27017)
    logging.info(f"Client: {client}")
    db: Database = client['bookstore']
    books: Collection = db['books']
    print_all_documents(books)
