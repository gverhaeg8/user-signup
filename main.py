from flask import Flask, request, redirect
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/', methods = ['GET', 'POST'])
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route('/valid-username', methods = ['GET', 'POST'])
def validate_signup():

    username_error=''
    password_error=''
    password2_error=''
    email_error=''
    
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']
        password2= request.form['verify']
        email= request.form['email']  

    if password2 != password:
        password2_error = 'Passwords do not match.'
    elif password2 == '':
        password2_error = "Password must be verified."
    else:
        password2= password2


    if len(password) >= 20 or len(password) <3:
        password_error = 'Password must be within 3-20 characters.'
    elif password == '':
        password_error = 'Invalid password.'
    else: 
        password == password
        password2 == password2

    if ' ' in password:
        password_error = 'Password cannot contain spaces.'

    if ' ' in username:
        username_error = 'Username cannot contain spaces.'
        

    if len(username) >= 20 or len(username) < 3:
        username_error = 'Username must be within 3-20 characters.'
        username = ''
    elif username == '':
        username_error = 'Invalid username.'
        username = ''
    else:
        username == username

    if email:
        if '@' not in email:
            email_error = "Email must contain '@'."
            email = ''
        elif '.' not in email:
            email_error = 'Email must contain a period.'
            email = ''
        elif ' ' in email:
            email_error = 'Email cannot have spaces.'
            email = ''
        elif len(email) >= 20 or len(email) < 3:
            email_error = 'Email must be within 3-20 characters.'
            email = ''
        else:
            email = email

    if email == '':
            email = email

    if not username_error and not password_error and not password2_error and not email_error:
        template = jinja_env.get_template('welcome.html')
        return template.render(username=username)
    else: 
        template = jinja_env.get_template('index.html')
        return template.render(password_error=password_error, username_error=username_error, email_error=email_error, password2_error=password2_error, username=username, password=password, email=email)


if __name__ == '__main__':
    app.run()