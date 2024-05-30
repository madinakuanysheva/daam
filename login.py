from flask import Blueprint, request, jsonify, session, redirect, url_for
import sqlite3

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def login_user():
    user_email = request.form.get('user_email')
    user_password = request.form.get('user_password')

    if not user_email or not user_password:
        return jsonify({'error': 'Missing email or password'}), 400

    conn = sqlite3.connect('daam.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_email=? AND user_password=?", (user_email, user_password))
    user = cursor.fetchone()
    conn.close()

    if user:
        session['user_id'] = user[0]
        return redirect(url_for('main'))  # Перенаправление на главную страницу
    else:
        return jsonify({'error': 'Invalid email or password'}), 401
