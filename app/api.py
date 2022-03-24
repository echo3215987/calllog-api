# coding:utf-8
import os
import json
from response import initResponse, parseResponseJson, setErrorResponse
from log import logging
import datetime
from sqlalchemy import create_engine
import pandas as pd

from flask import Flask, request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
app = Flask(__name__)

# swagger default setting
swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['title'] = 'Call Log API'
swagger_config['description'] = 'This document depicts Swagger UI. [Base URL: 10.109.6.10:33000/]'
swagger_config['version'] = '0.1'
swagger_config['schemes'] = ['HTTP']
# swagger_config['url'] = 'http://10.109.6.10:33000/apidocs/'

swagger = Swagger(app, config=swagger_config)

# daily inference
@swag_from("daily_inference.yml", methods=['POST'])
@app.route('/ai_inference/daily/', methods = ['POST'])
def daily_inference():
    data = json.loads(request.data)
    file_name = data['file_name']
#     print(type(data['inference_data']))
    db_df = pd.DataFrame(data['inference_data'])
    print(db_df)
    display(db_df)
#     db.to_sql()
    
    responseData = parseResponseJson(f"{file_name} is in inference queue.")
    return responseData

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=33000)
