from registration import register
from login import login
from logout import logout
from personal_info_and_chat import personal_info_and_chat

from database import create_app
from flask_cors import CORS
from flask import Flask, render_template

app = create_app()
CORS(app)

app.secret_key = 'your_secret_key'

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/registration_page')
def registration_page():
    return render_template('registration.html')

@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.route('/about_us')
def about_us():
    return render_template('about.html')

@app.route('/account_page')
def account_page():
    return render_template('personal_info_and_chat.html')




app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(personal_info_and_chat, url_prefix='/personal_info_and_chat')

if __name__ == '__main__':
    app.run(debug=True)
