from flask import request
import sqlite3
from flask import Blueprint, jsonify

register = Blueprint('register', __name__)


@register.route('/register', methods=['POST'])
def register_user():
    user_name = request.form.get('user_name')
    user_surname = request.form.get('user_surname')
    user_email = request.form.get('user_email')
    user_password = request.form.get('user_password')
    user_plan = request.form.get('user_plan', 'free')

    if not all([user_name, user_surname, user_email, user_password]):
        return 'Missing required fields', 400

    conn = sqlite3.connect('daam.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (user_name, user_surname, user_email, user_password, user_plan) VALUES (?, ?, ?, ?, ?)",
        (user_name, user_surname, user_email, user_password, user_plan)
    )
    conn.commit()
    conn.close()

    return jsonify({'message': 'Registration successful!'}), 200
