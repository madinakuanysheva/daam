import sqlite3
from flask import Blueprint, render_template, redirect, url_for, request, flash

register = Blueprint('register', __name__)

@register.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        user_surname = request.form.get('user_surname')
        user_email = request.form.get('user_email')
        user_password = request.form.get('user_password')
        user_plan = request.form.get('user_plan', 'free')

        if not all([user_name, user_surname, user_email, user_password]):
            flash('Missing required fields', 'error')
            return render_template('registration.html')

        conn = sqlite3.connect('daam.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name=?", (user_name,))
        existing_user = cursor.fetchone()

        if existing_user:
            error_message = "A user with this username already exists."
            conn.close()
            return render_template('registration.html', error_message=error_message)
        else:
            cursor.execute("INSERT INTO users (user_name, user_surname, user_email, user_password, user_plan) VALUES (?, ?, ?, ?, ?)",
                           (user_name, user_surname, user_email, user_password, user_plan))
            conn.commit()
            conn.close()
            flash('Registration successful!', 'success')
            return redirect(url_for('login.login_user'))





