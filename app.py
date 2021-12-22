import secrets
secret_key= secrets.token_urlsafe(16)
from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


@app.route('/')
def index():
      return render_template('index.html')