import sqlite3
from flask import Blueprint, render_template, session, redirect, url_for

personal_info_and_chat = Blueprint('personal_info_and_chat', __name__)


@personal_info_and_chat.route('/personal_info_and_chat')
def show_personal_info_and_chat():
    if 'user_id' not in session:
        return redirect(url_for('login.login_page'))  # Если пользователь не аутентифицирован, перенаправляем на страницу входа

    user_id = session['user_id']  # Получаем id пользователя из сессии
    conn = sqlite3.connect('your_database.db')  # Подключаемся к вашей базе данных
    cursor = conn.cursor()

    # Выполняем SQL-запрос для получения электронной почты пользователя по его id
    cursor.execute("SELECT user_email FROM users WHERE id = ?", (user_id,))
    user_email = cursor.fetchone()[0]  # Получаем первый столбец из первой строки результата запроса

    conn.close()  # Закрываем соединение с базой данных

    return render_template('personal_info_and_chat.html', user_email=user_email)


