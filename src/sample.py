from pymongo import MongoClient
import logging

_log = logging.getLogger(__name__)

DATABASE = 'EMPLOYEE'
TABLE = 'COREVIEW'

def connect():
    try:
        _log.info("Connection is processing....")
        client = MongoClient('0.0.0.0', 27017)
        print(client)

        if client:
            _log.info("Connection successfully established.")
            print("Connection successfully established.")
        else:
            _log.info("Connection not established.")
            print("Connection not established.")

        db = client.bussiness

        fivestar = db.reviews.find_one({'rating': 5})
        print(fivestar)

    except Exception as e:
        _log.error(e), 404


if __name__ == '__main__':
    connect()