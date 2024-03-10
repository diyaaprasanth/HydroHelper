from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField, validators
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash
import matplotlib.pyplot as plt
import numpy as np


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
                usage = shower + bathroom + dishwasher + laundry + other
                return f"usage: {usage}"
            return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run()
