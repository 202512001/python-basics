from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Amit", "marks": 78},
    {"id": 2, "name": "Shruti", "marks": 90}
]

@app.route("/api/students")
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)