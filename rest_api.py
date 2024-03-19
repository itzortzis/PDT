
from flask import Flask, jsonify
from app.main import main


app = Flask(__name__)

@app.route('/run')
def test():
   path = main()
   return jsonify({ 'output': path }), 400

# @app.route('/set/<username>')
# def insert(username):
#    print("New Request arrived")
#    data = {
#       'username': username
#    }
   
#    return jsonify(data), 400

if __name__ == '__main__':
   # Production mode
   # from waitress import serve
   # serve(app, host="0.0.0.0", port=5000)
   
   # Debugging mode
   app.run(port=5000)

