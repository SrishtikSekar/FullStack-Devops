from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/student-details', methods=['GET'])
def student():
    return jsonify({
        "name": "Srishtik Sekar",
        "roll": "2023BCS0220",
        "register": "YOUR_REGISTER_NO"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)