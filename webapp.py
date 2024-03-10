'''
from flask import Flask
import csv

app = Flask(__name__)


@app.route('/')
def read_file():
    file_path = 'gridData.csv'  # Replace 'example.txt' with the path to your file
    
    try:
        with open(file_path, 'r') as file:
            content = csv.reader(file_path)
            demand = next(next(content))
            print( "AAAAAAAAA")
            return f"File content:\n\n{content}"

    except FileNotFoundError:
        return f"File not found at path: {file_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
'''
from flask import Flask, render_template, request 
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField 
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField 
from wtforms.validators import InputRequired 
from werkzeug.security import generate_password_hash 
  
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'secretkey'
  
  
class MyForm(FlaskForm): 
    name = StringField('Name', validators=[InputRequired()]) 
    password = PasswordField('Password', validators=[InputRequired()]) 
    remember_me = BooleanField('Remember me') 
    salary = DecimalField('Salary', validators=[InputRequired()]) 
    gender = RadioField('Gender', choices=[ 
                        ('male', 'Male'), ('female', 'Female')]) 
    country = SelectField('Country', choices=[('IN', 'India'), ('US', 'United States'), 
                                              ('UK', 'United Kingdom')]) 
    message = TextAreaField('Message', validators=[InputRequired()]) 
    photo = FileField('Photo') 
  

@app.route('/', methods=['GET', 'POST']) 
def index(): 
    form = MyForm() 
    if form.validate_on_submit(): 
        name = form.name.data 
        password = form.password.data 
        remember_me = form.remember_me.data 
        salary = form.salary.data 
        gender = form.gender.data 
        country = form.country.data 
        message = form.message.data 
        photo = form.photo.data.filename 
        return f'Name: {name} < br > Password: {generate_password_hash(password)} <br > Remember me: {remember_me} < br > Salary: {salary} < br > Gender: {gender} <br > Country: {country} < br > Message: {message} < br > Photo: {photo}' 
    return render_template('index.html', form=form) 
  
  
if __name__ == '__main__': 
    app.run() 
