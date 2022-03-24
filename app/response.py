# coding:utf-8
import json

def initResponse():
    responseData = {}
    responseData['responseCode'] = 200
    responseData['responseMessage'] = 'OK'
    return responseData

def parseResponseJson(result):
    responseData = initResponse()
    responseData['result'] = result
    return json.dumps(responseData, ensure_ascii=False).encode('utf8')

def setErrorResponse(errorCode, errorMessage):
    responseData = {}
    responseData['responseCode'] = errorCode
    responseData['responseMessage'] = errorMessage
    return json.dumps(responseData, ensure_ascii=False).encode('utf8')
