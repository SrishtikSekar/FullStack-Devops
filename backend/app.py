from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/student-details', methods=['GET'])
def student():
    return jsonify({
        "name": "Srishtik Sekar",
        "roll": "2023BCS0220",
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)