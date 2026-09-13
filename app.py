"""A minimal Flask application for learning Docker fundamentals."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render the application home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
