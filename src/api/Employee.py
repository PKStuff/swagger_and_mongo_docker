import connexion
import logging
from flask import request, abort
from common import connect

_log = logging.getLogger(__name__)

client, mydb, mycollection = connect()

def addEmp(empId, name):
    try:
        if client:
            rec = {
                "empId" : empId,
                "name" : name
            }

            record = mydb.mycollection.insert(rec)
            response = {
                "message": "Employee Added"
            }
        
        else:
            response = {
                "message": "Employee not added"
            }
        return response
    except Exception as e:
        _log.error(e)
        return {"message":'bad data'}, 404


def getEmpById(empId):
    try:
        if client:
            record = mydb.mycollection.find_one({'empId': empId})
            if record:
                response = {
                    "empId" : record['empId'],
                    "name" : record['name']
                }
            else:
                response = {
                    "Message" : "Employee Not Found."
                }
        
        else:
            response = {
                "Message": "Connection not established.."
            }
        
        return response
    except Exception as e:
        _log.error(e)
        return {"message":'bad data'}, 404

def deleteEmp(empId):
    try:
        if client:
            record = mydb.mycollection.remove({'empId': empId})

            if record:
                response = {
                    "message": "Employee Deleted"
                }
            else:
                response = {
                   "message": "Employee Not found."
                }
        else:
            response = {
                "Message": "Connection not established.."
            }
            
        return response
    except Exception as e:
        _log.error(e)
        return {"message":'bad data'}, 404

def updateEmployee(empId, name):
    try:
        if client:
            record = mydb.mycollection.update({'empId':empId}, {"$set":{'name': name}})
            if record:
                response = {
                    "message": "Employee Updated"
                }
            else:
                response = {
                    "message" : "Employee not found"
                }
        else:
            response = {
                "Message": "Connection not established.."
            }
            
        return response
    except Exception as e:
        _log.error(e)
        return {"message":'bad data'}, 404

def getAllEmp():
    try:
        if client:
            record = mydb.mycollection.find()
            if record:
                response_list = []
                for records in record:
                    response_dict = {
                        "empId" : records['empId'],
                        "name" : records['name']
                    }
                    response_list.append(response_dict)
                return response_list
            else:
                return {
                    "Message" : "Employee Not Found."
                }
        
        else:
            return {
                "Message": "Connection not established.."
            }
    except Exception as e:
        _log.error(e)
        return {"message":'bad data'}, 404
