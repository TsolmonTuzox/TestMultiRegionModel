from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'Example Data',
        'value': 42
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)