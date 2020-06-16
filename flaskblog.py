from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = ''

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

if __name__ == '__main__':
    app.run(debug=True)
