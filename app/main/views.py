from flask import render_template, url_for, redirect
from . import main
from .forms import Login_Form, Registration_Form

# all routes of page

#------------------------------------------------------------- index
@main.route('/')
@main.route('/home/')
def index():
    user_name = 'suvasish'
    return render_template('index.html', user_name=user_name)


#------------------------------------------------------------- blog
@main.route('/blog/')
def blog():
    return render_template('blog.html')


#------------------------------------------------------------- posts
@main.route('/post/')
def post():
    return render_template('post.html')


# ----------------------------------------------------------- login
@main.route('/login/', methods=['GET','POST'])
def login():
    form = Login_Form()

    # GET request action
    if form.validate_on_submit():
        print("Email: "+form.login_form_email.data)
        print("Password: "+form.login_form_pass.data)

        # reseting all data to empty str
        form.login_form_email.data=''
        form.login_form_pass.data=''

        # redirect session
        return redirect(url_for('main.index'))

    return render_template('login.html', form=form)


# ------------------------------------------------------------ registration
@main.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = Registration_Form()

    # GET request action
    if form.validate_on_submit():
        print('Name: '+form.registration_form_name.data)
        print('Email: '+form.registration_form_email.data)
        print('Pass: '+form.registration_form_pass.data)

        # reseting all data to empty str
        form.registration_form_name.data=''
        form.registration_form_email.data=''
        form.registration_form_pass.data=''
        form.registration_form_cpass.data=''

        # redirect page
        return redirect(url_for('main.login'))
    return render_template('registration.html', form=form)


#------------------------------------------------------------- about
@main.route('/about/')
def about():
    return render_template('about.html')


#------------------------------------------------------------- feedback
@main.route('/feedback')
def feedback():
    return render_template('feedback.html')

# ------------------------------------------------------------ user
@main.route('/user/')
@main.route('/user/<user_name>')
def user(user_name):
    return render_template('user.html', user_name = user_name)