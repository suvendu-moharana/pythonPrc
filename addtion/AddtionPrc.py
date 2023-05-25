from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add_number():
    data = request.get_json()
    n1 = data['n1']
    n2 = data['n2']
    result = n1 + n2
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
