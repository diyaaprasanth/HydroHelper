from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import (
    DecimalField,
    RadioField,
    SelectField,
    TextAreaField,
    FileField,
    validators,
)
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash
from matplotlib.figure import Figure
from io import BytesIO
import numpy as np
import base64

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"


class MyForm(FlaskForm):

    action1 = SelectField(
        "Source",
        choices=[
            ("Select", "Select"),
            ("Bathroom", "Bathroom"),
            ("Shower", "Shower"),
            ("Dishwasher", "Dishwasher"),
            ("Laundry", "Laundry"),
            ("Other", "Other"),
        ],
        default="Select",
    )
    time1 = DecimalField("Time/Amount of Times", validators=[DataRequired()])
    action2 = SelectField(
        "Source",
        choices=[
            ("Select", "Select"),
            ("Bathroom", "Bathroom"),
            ("Shower", "Shower"),
            ("Dishwasher", "Dishwasher"),
            ("Laundry", "Laundry"),
            ("Other", "Other"),
        ],
        default="Select",
    )
    time2 = DecimalField("Time/Amount of Times", validators=[validators.optional()])
    action3 = SelectField(
        "Source",
        choices=[
            ("Select", "Select"),
            ("Bathroom", "Bathroom"),
            ("Shower", "Shower"),
            ("Dishwasher", "Dishwasher"),
            ("Laundry", "Laundry"),
            ("Other", "Other"),
        ],
        default="Select",
    )
    time3 = DecimalField("Time/Amount of Times", validators=[validators.optional()])
    action4 = SelectField(
        "Source",
        choices=[
            ("Select", "Select"),
            ("Bathroom", "Bathroom"),
            ("Shower", "Shower"),
            ("Dishwasher", "Dishwasher"),
            ("Laundry", "Laundry"),
            ("Other", "Other"),
        ],
        default="Select",
    )
    time4 = DecimalField("Time/Amount of Times", validators=[validators.optional()])
    action5 = SelectField(
        "Source",
        choices=[
            ("Select", "Select"),
            ("Bathroom", "Bathroom"),
            ("Shower", "Shower"),
            ("Dishwasher", "Dishwasher"),
            ("Laundry", "Laundry"),
            ("Other", "Other"),
        ],
        default="Select",
    )
    time5 = DecimalField("Time/Amount of Times", validators=[validators.optional()])
    submit = SubmitField("Submit")

    @app.route("/", methods=["GET", "POST"])
    def index():
        form = MyForm()
        # shower is 2.5 gallons/min, bathroom 1.6 gallons/flush, dishwasher = 6 gallons/load, laundry = 20 gallons/load, other = 10 gallons
        if form.validate_on_submit():
            action1 = form.action1.data
            time1 = form.time1.data
            action2 = form.action2.data
            time2 = form.time2.data
            action3 = form.action3.data
            time3 = form.time3.data
            action4 = form.action4.data
            time4 = form.time4.data
            action5 = form.action5.data
            time5 = form.time5.data
            actionList = [action1, action2, action3, action4, action5]
            timeList = [time1, time2, time3, time4, time5]
            shower = 0
            bathroom = 0
            dishwasher = 0
            laundry = 0
            other = 0
            for value, item in enumerate(actionList):
                if item == "Shower":
                    shower = 2.5 * int(timeList[value])
                elif item == "Bathroom":
                    bathroom = 1.6 * int(timeList[value])
                elif item == "Dishwasher":
                    dishwasher = 6 * int(timeList[value])
                elif item == "Laundry":
                    laundry = 20 * int(timeList[value])
                elif item == "Other":
                    other = 10 * int(timeList[value])

            source_of_usage = ["Shower", "Bathroom", "Dishwasher", "Laundry", "Other"]
            usage = [shower, bathroom, dishwasher, laundry, other]
            usageTotal = shower + bathroom + dishwasher + laundry + other

            fig = Figure(figsize=(10, 5))
            ax = fig.subplots()
            ax.bar(
                source_of_usage,
                usage,
                color=("#8FD0CA", "#5AC6C6", "#42ABC5", "#40B5BC", "#D3DACE"),
                width=0.4,
            )

            ax.set_xlabel("Source of Usage")
            ax.set_ylabel("Usage in Gallons")
            ax.set_title("Water Consumption per Action")
            ax.text(
                0.5,
                0.9,
                f"Your Total Water Consumption : {usageTotal} gallons",
                horizontalalignment="center",
                verticalalignment="center",
                transform=ax.transAxes,
                fontsize=12,
            )
            ax.plot()

            buf = BytesIO()
            fig.savefig(buf, format="png")
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return f"<img src='data:image/png;base64,{data}'/>"

        return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run()
