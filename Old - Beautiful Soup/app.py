# dependencies
from flask import Flask, render_template

# set up Flask app
app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('index.html')

# scraped route
@app.route('/scraped')
def scraped():
    return render_template('scraped.html')

if __name__ == "__main__":
    app.run(debug=True)