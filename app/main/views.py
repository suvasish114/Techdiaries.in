from flask import render_template, url_for, redirect
from . import main
from .forms import Login_Form
# from .. import db
from ..models import Admin, db

# all routes of page

#------------------------------------------------------------- index
@main.route('/')
@main.route('/home/')
def index():
    return render_template('index.html')


#------------------------------------------------------------- blog
@main.route('/blog/')
def blog():
    return render_template('blog.html')


#------------------------------------------------------------- posts
@main.route('/post/')
def post():
    return render_template('post.html')

# ----------------------------------------------------------- Admin
@main.route('/admin/', methods=['GET','POST'])
def admin():
    form = Login_Form()

    # GET request action
    if form.validate_on_submit():
        print('-'*10)
        print('Admin Id: '+form.login_form_id.data)
        print('Password: '+form.login_form_pass.data)
        print('-'*10)


        # storing in database
        my_user = Admin(admin_id = form.login_form_id.data, admin_password = form.login_form_pass.data)
        db.session.add(my_user)
        db.session.commit()

        return render_template('index.html')
    return render_template('admin.html', form=form)

# ----------------------------------------------------------- login
# @main.route('/login/', methods=['GET','POST'])
# def login():
#     form = Login_Form()

#     # GET request action
#     if form.validate_on_submit():
#         print("Email: "+form.login_form_email.data)
#         print("Password: "+form.login_form_pass.data)

#         # storing in database
#         # db.create_all()
#         my_user = User(email = form.login_form_email.data, password = form.login_form_pass.data)
#         db.session.add(my_user)
#         db.session.commit()
        
#         # reseting all data to empty str
#         form.login_form_email.data=''
#         form.login_form_pass.data=''

#         # redirect session
#         return redirect(url_for('main.index'))

#     return render_template('login.html', form=form)


# # ------------------------------------------------------------ registration
# @main.route('/registration/', methods=['GET', 'POST'])
# def registration():
#     form = Registration_Form()

#     # GET request action
#     if form.validate_on_submit():
#         print('Name: '+form.registration_form_name.data)
#         print('Email: '+form.registration_form_email.data)
#         print('Pass: '+form.registration_form_pass.data)

#         # reseting all data to empty str
#         form.registration_form_name.data=''
#         form.registration_form_email.data=''
#         form.registration_form_pass.data=''
#         form.registration_form_cpass.data=''

#         # redirect page
#         return redirect(url_for('main.login'))
#     return render_template('registration.html', form=form)


#------------------------------------------------------------- about
@main.route('/about/')
def about():
    return render_template('about.html')


#------------------------------------------------------------- feedback
@main.route('/feedback')
def feedback():
    return render_template('feedback.html')

# ------------------------------------------------------------ user
# @main.route('/user/')
# @main.route('/user/<user_name>')
# def user(user_name):
#     return render_template('user.html', user_name = user_name)