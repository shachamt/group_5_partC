from flask import Blueprint, render_template, redirect, url_for, session

# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')


# Routes
@homepage.route('/')
def index():
    session['logedin'] = False
    session['isMani'] = False
    session['email'] =' '
    return redirect('/homepage')


@homepage.route('/homepage')
def redirect_homepage():
    return render_template('homepage.html')