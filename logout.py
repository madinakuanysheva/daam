from flask import session
from flask import Blueprint

logout = Blueprint('logout', __name__)


@logout.route('/logout')
def logout_user():
    session.pop('user_id', None)
    return ' You have sucessfully logout!'
