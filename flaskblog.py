from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c269614952714198f3f630b5e7704eec'

posts = [
    {
        'author': 'Alec Wells',
        'title': 'Blog Post 1',
        'content': 'First content',
        'date_posted': 'June 9, 2020'
    },
    {
        'author': 'Alec Wellsssss',
        'title': 'Blog Post 1ssss',
        'content': 'First contentsssss',
        'date_posted': 'June 9, 2020sssss'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit()
        flash(f'Account created for  {form.username.data}!', 'success')

    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = RegistrationForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
