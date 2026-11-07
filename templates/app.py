from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret-key-123"

@app.route("/")
def index():
    context = {
        "title": "Головна сторінка подій",
        "events_count": 3,
        "organizer": "IT Hub Ukraine",
        "year": datetime.now().year
    }
    return render_template("index.html", **context)

@app.route("/events")
def events_list():
    events_data = [
        {"name": "Python Meetup", "price": 0, "active": True},
        {"name": "AI Conference", "price": 450, "active": True},
        {"name": "Frontend Workshop", "price": 200, "active": False}
    ]
    context = {
        "title": "Список подій",
        "events": events_data,
        "year": datetime.now().year
    }
    return render_template("events.html", **context)

if __name__ == "__main__":
    app.run(debug=True, port=5000)