from flask import Blueprint, request, render_template, redirect, url_for, session, flash
import sqlite3

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        user_email = request.form.get('user_email')
        user_password = request.form.get('user_password')

        if not user_email or not user_password:
            flash('Отсутствует email или пароль', 'error')
            return redirect(url_for('login.login_user'))

        conn = sqlite3.connect('daam.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_email=? AND user_password=?", (user_email, user_password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            flash('You have logged in as {}'.format(user_email), 'success')
            return redirect(url_for('main'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('login.login_user'))

    return render_template('login.html')

