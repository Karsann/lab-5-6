from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret-key-123"


class EventRegistrationForm(FlaskForm):
    name = StringField(
        "Ваше ім'я",
        validators=[
            DataRequired(message="Поле імені обов'язкове"),
            Length(min=2, max=50, message="Ім'я має містити від 2 до 50 символів")
        ]
    )
    email = EmailField(
        "Електронна пошта",
        validators=[
            DataRequired(message="Введіть email"),
            Email(message="Некоректний формат email")
        ]
    )
    event = SelectField(
        "Оберіть подію",
        choices=[
            ("python", "Python Meetup"),
            ("ai", "AI Conference"),
            ("frontend", "Frontend Workshop")
        ]
    )
    comment = TextAreaField(
        "Побажання / Коментар",
        validators=[Length(max=200, message="Коментар не може перевищувати 200 символів")]
    )
    submit = SubmitField("Зареєструватися")

    def validate_name(self, field):
        if any(char.isdigit() for char in field.data):
            raise ValidationError("Ім'я не повинно містити цифр")

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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = EventRegistrationForm()
    if form.validate_on_submit():
        flash(f"Дякуємо, {form.name.data}! Ви успішно зареєструвалися.", "success")
        return redirect(url_for("register"))
    return render_template("register.html", form=form, title="Реєстрація", year=datetime.now().year)

if __name__ == "__main__":
    app.run(debug=True, port=5000)