from pymongo import MongoClient
import logging

_log = logging.getLogger(__name__)

DATABASE = 'EMPLOYEE'
TABLE = 'COREVIEW'

def connect():
    try:
        _log.info("Connection is processing....")
        client = MongoClient('mongo:27017')

        if client:
            _log.info("Connection successfully established.")
        else:
            _log.info("Connection not established.")

        mydatabase = client[DATABASE]

        mycollection = mydatabase[TABLE]

        return client, mydatabase, mycollection

    except Exception as e:
        _log.error(e), 404
