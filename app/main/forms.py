from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# for login page
class Login_Form(FlaskForm):
    login_form_email = StringField('Email', validators=[DataRequired()])
    login_form_pass = StringField('Password', validators=[DataRequired()])
    login_form_submit = SubmitField('Login')

# for register page
class Registration_Form(FlaskForm):
    registration_form_name = StringField('Name', validators=[DataRequired()])
    registration_form_email = StringField('Email', validators=[DataRequired()])
    registration_form_pass = StringField('Password', validators=[DataRequired()])
    registration_form_cpass = StringField('Confirm Password', validators=[DataRequired()])
    registration_form_submit = SubmitField('Create Account')