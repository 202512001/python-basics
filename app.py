from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home working"

@app.route("/about")
def about():
    return "About working"

@app.route("/api/info")
def info():
    return jsonify({"status": "API working",
                     "name": "Shruti",
                     "role": "Backend Developer",
                    "skill": "Python + Flask"})
@app.route("/api/greet/<name>")
def greet(name):
    return jsonify({
                "message": f"Hello {name}"
                  })

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


