from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
import connexion

app = connexion.App(__name__, specification_dir='./swagger/')

app.add_api('swagger.yaml')

@app.route('/')
def hello_flask():
    return 'Hello Flask!!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8084)