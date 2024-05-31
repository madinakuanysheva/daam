import sqlite3
from flask import Blueprint, render_template, session, redirect, url_for

personal_info_and_chat = Blueprint('personal_info_and_chat', __name__)


@personal_info_and_chat.route('/personal_info_and_chat')
def show_personal_info_and_chat():
    if 'user_id' not in session:
        return redirect(url_for('login.login_page'))

    user_id = session['user_id']
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT user_email FROM users WHERE id = ?", (user_id,))
    user_email = cursor.fetchone()[0]

    conn.close()
    return render_template('personal_info_and_chat.html', user_email=user_email)


