from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcometokodekloud():
    return "Welcome to KodeKloud!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)