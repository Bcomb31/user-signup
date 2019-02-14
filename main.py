from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def display_signup_form():
    return render_template('index.html')


def validate(user_pass):
    try:
        (user_pass)
        print(user_pass)
        return True
    except ValueError:
        return False

@app.route('/', methods=['POST'])
def validate_signup():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if  username =="":
        print("yes")
        username_error = 'Please enter username'
        username = ''
       
    elif len(username) < 3 or len(username) > 20:
        username_error = 'username not correct length please enter between 3 to 20 characters'
        username = ''

    elif " " in username:
        username_error = 'No Spaces please'
        username = ''

    if password =="":
        password_error = 'Please enter password'
        password = ''
    else:
        if  password != verify:
            verify_error = 'passwords do not match, please re-enter'
            verify = ''

        elif len(password) < 3 or len(password) > 20:
                password_error = 'password not correct length please enter between 3 to 20 characters'
                password = ''

    if len(email):

        length_and_spaces_bool = email
        print(length_and_spaces_bool)
       
        at_and_dot_bool = False
       
        if "@" in email and "." in email:
            if email.count("@") == 1 and email.count(".") == 1:
                at_and_dot_bool = True

        if not length_and_spaces_bool or not at_and_dot_bool:
            email_error = 'You have entered an invalid email.'
            email = ''
        if " " in email:
            email_error = 'You have entered a space - invalid email.'
            email = ''
    if not password_error and not verify_error and not username_error and not email_error:
        return redirect("/welcome?name={0}".format(username))
    else:
        return render_template('index.html', username_error=username_error,
            password_error=password_error, verify_error=verify_error, email_error = email_error, 
            username=username,
            password=password, email=email)

@app.route('/welcome')
def welcome():
    username = request.args.get('name')
    return render_template('welcome.html', username = username)

app.run()