#!/usr/bin/env python3


from flask import Flask,render_template, url_for

app = Flask(__name__)

posts=[{
    "author":"Dianah",
    "title":"Africa kills her sun",
    "content":"Blog post 1",
    "date_posted":"Oct 11, 2022"
    },
    {
    "author":"Jane Doh",
    "title":"48 laws of power",
    "content":"Blog post 2",
    "date_posted":"Oct 12, 2022"
    }
    ]

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about_page():
    return render_template('about.html', title="about page")

if __name__=='__main__':
    app.run(debug=True)

