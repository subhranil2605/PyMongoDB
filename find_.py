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
    my_db: Database = client[database_name]

    collection_name: str = "customers"
    customers: Collection = my_db[collection_name]

    # find one (first occurence)
    x = customers.find_one()
    logging.debug(x)

    # find all
    for customer in customers.find():
        logging.debug(customer)

    # only some fields
    for customer in customers.find({}, {"_id": 0, "name": 1}):
        logging.debug(customer)

    # query
    for x in customers.find({"address": "Krishnagar"}):
        print(x)

    # query with some specific values
    for x in customers.find({"address": "Krishnagar"}, {"_id": 0}):
        print(x)
