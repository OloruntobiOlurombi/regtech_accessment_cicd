import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

secret_key = os.getenv('SECRET_KEY')
if secret_key is None:
    raise ValueError("No SECRET_KEY set for Flask application. Please set the SECRET_KEY environment variable.")
app.config['SECRET_KEY'] = secret_key

csrf = CSRFProtect(app)

@app.route('/')
def hello():
    return "Hello, Welcome to Zip Reg Tech!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
