from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
import logging
from utils import print_all_documents

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")

if __name__ == '__main__':
    client: MongoClient = MongoClient('localhost', 27017)
    logging.info(f"Client: {client}")
    db: Database = client['bookstore']
    books: Collection = db['books']
    print_all_documents(books)
