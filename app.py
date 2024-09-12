import os
from flask import Flask 
from flask_wtf.csrf import CSRFProtect
import secrets

app = Flask(__name__)


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', secrets.token_urlsafe(32))

csrf = CSRFProtect(app)

@app.route('/')
def hello():
    return "Hello, Welcome to Zip Reg Tech!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)