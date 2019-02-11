from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


app = Flask(__name__)
app.config['DEBUG'] = True


signup_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Signup</h1>
    <form method='POST'>
        <label>Username
            <input name="username" type="text" value='{username}' />
        </label>
        <p class="error">{username_error}</p>
        <label>Password
            <input name="password" type="text" value='{password}' />
        </label>
        <br>
        <br>
        <label for="verify">Verify Password</label>
            <input name="verify" type="password" />
        <p class="error">{password_error}</p>
        <label for="email">Email (optional)</label>
        <input name="email" value="">
        <br>
        <input type="submit" value="Submit" />
    </form>
    """

@app.route('/')
def display_signup_form():
    return signup_form.format(username='', username_error='',
        password='', verify='', password_error='', email='')


def validate(num):
    try:
        (num)
        print(num)
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

    if  username == "":
        print("yes")
        username_error = 'Please enter a username'
        username = ''
        return signup_form.format(username_error=username_error)
    if len(username) < 3 or len(username) > 20:
        username_error = 'username not correct length please enter between 3 to 20 characters'
        username = ''

    if not validate(password):
        password_error = 'Not a valid password'
        password = ''
    else:
        if not password == verify:
            password_error = 'passwords do not match, please re-enter'
            verify = ''

        if len(password) < 3 or len(password) > 20:
                password_error = 'password not correct length please enter between 3 to 20 characters'
                password = ''
        

    if not password_error and not username_error:
        return ("Welcome, " + (username))
    else:
        return signup_form.format(username_error=username_error,
            password_error=password_error,
            username=username,
            password=password)


app.run()