from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
import logging
from utils import check_database_exists, insert
from pymongo.results import InsertOneResult, InsertManyResult

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")

if __name__ == '__main__':
    client: MongoClient = MongoClient('localhost', 27017)
    logging.info(f"Client: {client}")

    database_name: str = "mydb"

    if check_database_exists(client, database_name):
        logging.critical(f"Database is already exists: {database_name}!!!")
    else:
        logging.info(f"There's no database named as: {database_name}")

    my_db: Database = client[database_name]

    # creating a collection
    collection_name: str = "customers"
    my_col: Collection = my_db[collection_name]

    # show all the collections
    # print(my_db.list_collection_names())

    # inserting single document
    # my_dict = {"name": "Ashik Mamun", "address": "Krishnagar"}
    # result: InsertOneResult = insert(my_col, my_dict)
    # logging.debug(result.inserted_id)

    # inserting multiple documents
    data = [
        {"name": "Sumit Saha", "address": "Shyamnagar"},
        {"name": "Arpan Manna", "address": "Srerampore"}
    ]
    result: InsertManyResult = insert(my_col, data)
    logging.debug(result.inserted_ids)
