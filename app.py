from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hi, I’m Shobhit. This app is deployed using DevOps tools."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
