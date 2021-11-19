from flask import request, render_template, flash
from .models.loginform import LoginForm
from . import practice01

@practice01.route('/index')
def index():
    return render_template('index.html')

@practice01.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        print(request.data.get('username'))
        print(request.args.get('password'))
        print(request.args.get('password2'))
        if login_form.validate_on_submit():
            flash('success')
        else:
            flash(login_form.errors)
    return render_template('login.html',login_form=login_form)
