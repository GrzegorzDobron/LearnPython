from flask import Flask, jsonify, request

app = Flask(__name__)
database = [
    {
        "fileName": "fileName_demo",
        "contents": "contents_demo",
    }
]

@app.route('/database')
def home():
    return jsonify(database)

@app.route('/songs', methods=['POST'])
def add_songs():
    newRecord = request.get_json()
    database.append(newRecord)
    return jsonify(database)

if __name__ == '__main__':
  app.run(debug=True)