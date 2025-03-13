from flask import Flask, jsonify, request
import jsonify


app = Flask(__name__)


@app.route('/',methods=['post', 'GET'])
def api():
   if request.method == 'POST':
       payload = request.json
       print("Testing it works",payload)
       return payload, 200
    elif request.method == 'GET':
        response_data = {
            "mesage": "This is the README for GET"
        }
        return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'), host='0.0.0', port=5000)
