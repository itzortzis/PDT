
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
   return jsonify({ 'error': 'Invalid employee properties.' }), 400

@app.route('/set')
def insert():
   return jsonify({ 'error': 'Invalid employee properties.' }), 400

if __name__ == '__main__':
   app.run(port=5000)

