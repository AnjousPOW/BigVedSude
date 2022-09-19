from flask import Flask, render_template, request, redirect, url_for
from messageForm import MessageForm
from user import User
from post import Post
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)

users = []
post = []

app.config['SECRET_KEY'] = 'Your secret key'


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', posts=post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add_user', methods=['GET', 'POST'])
def produsers():
    form = MessageForm()
    if form.validate_on_submit():
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        users.append(User(email, name, password))
        return redirect(url_for('produsers'))

    return render_template('add_user.html', form=form)



@app.route('/post', methods=['GET', 'POST'])
def prodpost():
    if request.method == 'POST':
        name = request.form.get('name')
        text = request.form.get('text')
        data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        user_name = request.form.get('user_name')

        for user in users:
            if user.name == user_name:
                post.append(Post(name, text, data, user.name))
                break
        else:
            return render_template('post_examination.html', post=post)
    print(post)

    return render_template('post.html', post=post)



@app.route('/users')
def users_handler():
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run()