from flask import Flask, render_template, request 
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField 
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField 
from wtforms.validators import InputRequired 
from werkzeug.security import generate_password_hash 
  
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'secretkey'
  
  
class MyForm(FlaskForm):
    def __init__(self):

            action1 = SelectField("Source",choices=[
                    ("Select", "Select"),
                    ("Bathroom", "Bathroom"),
                    ("Shower", "Shower"),
                    ("Dishwasher", "Dishwasher"),
                    ("Laundry", "Laundry"),
                    ("Other", "Other"), ],default="Select",)
            time1 = DecimalField('Time/Amount of Times', validators=[InputRequired()]) 
            action2 = SelectField("Source",choices=[
                    ("Select", "Select"),
                    ("Bathroom", "Bathroom"),
                    ("Shower", "Shower"),
                    ("Dishwasher", "Dishwasher"),
                    ("Laundry", "Laundry"),
                    ("Other", "Other"), ],default="Select",)
            time2 = DecimalField('Time/Amount of Times', validators=[InputRequired()])
            action3 = SelectField("Source",choices=[
                    ("Select", "Select"),
                    ("Bathroom", "Bathroom"),
                    ("Shower", "Shower"),
                    ("Dishwasher", "Dishwasher"),
                    ("Laundry", "Laundry"),
                    ("Other", "Other"), ],default="Select",)
            time3 = DecimalField('Time/Amount of Times', validators=[InputRequired()])
            action4 = SelectField("Source",choices=[
                    ("Select", "Select"),
                    ("Bathroom", "Bathroom"),
                    ("Shower", "Shower"),
                    ("Dishwasher", "Dishwasher"),
                    ("Laundry", "Laundry"),
                    ("Other", "Other"), ],default="Select",)
            time4 = DecimalField('Time/Amount of Times', validators=[InputRequired()])
            action5 = SelectField("Source",choices=[
                    ("Select", "Select"),
                    ("Bathroom", "Bathroom"),
                    ("Shower", "Shower"),
                    ("Dishwasher", "Dishwasher"),
                    ("Laundry", "Laundry"),
                    ("Other", "Other"), ],default="Select",)
            time5 = DecimalField('Time/Amount of Times', validators=[InputRequired()])

            @app.route('/', methods=['GET', 'POST']) 
                    def index(): 
                            form = MyForm() 
                            # shower is 2.5 gallons/min, bathroom`1.6 gallons/flush, dishwasher = 6 gallons/load, laundry = 20 gallons/load, other = 10 gallons
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
                   for value, item in enumerate(actionList):
                                    if item == "Shower":
                                             self.shower = 2.5*int(timeList[value])
                                    elif item == "Bathroom":
                                             self.bathroom = 1.6*int(timeList[value])
                                    elif item == "Dishwasher":
                                             self.dishwasher = 6*int(timeList[value])
                                    elif item == "Laundry":
                                             self.laundry = 20*int(timeList[value])
                                    else:
                                             self.other = 10*int(timeList[value])
                   self.shower = shower
                   self.bathroom = bathroom
                   self.dishwasher = dishwasher
                   self.laundry = laundry
                   self.other = other

                   usage = self.shower+self.bathroom+self.dishwasher+self.laundry+self.other	
                   return data, f'usage: {usage}'
            return render_template('index.html', form=form) 
  
if __name__ == '__main__': 
    app.run() 
    import numpy as np
    import matplotlib.pyplot as plt
        
        
    # creating the dataset 
    data = {'Shower':shower, 'Bathroom':bathroom, 'Dishwasher':dishwasher,'Laundry':laundry, 'Other': other}
    source_of_usage = list(data.keys())
    usage = list(data.values())
        
    fig = plt.figure(figsize = (10, 5))
        
    # creating the bar plot
    plt.bar(source_of_usage, usage, color =('#8FD0CA', '#5AC6C6', '#42ABC5', '#40B5BC', '#D3DACE'),  width = 0.4)
    plt.xlabel("Source of Usage")
    plt.ylabel("Usage in Gallons")
    plt.title("Water Consumption per Action")
    plt.show()
                       

