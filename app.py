from flask import Flask
from registration import register
from login import login
from logout import logout
from database import create_app

app = create_app()
app.secret_key = 'your_secret_key'


app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(logout)

if __name__ == '__main__':
    app.run(debug=True)