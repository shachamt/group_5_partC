from datetime import timedelta
from flask import Flask, session, redirect

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

###### Pages
## Homepage
from pages.homepage.homepage import homepage

app.register_blueprint(homepage)

## sign_in
from pages.sign_in.sign_in import sign_in

app.register_blueprint(sign_in)

## sign_up
from pages.sign_up.sign_up import sign_up

app.register_blueprint(sign_up)

## mani_results
from pages.mani_results.mani_results import mani_results

app.register_blueprint(mani_results)

## business_profile
from pages.business_profile.business_profile import business_profile

app.register_blueprint(business_profile)

## search_mani
from pages.search_mani.search_mani import search_mani

app.register_blueprint(search_mani)

###### Conponents
## Header
from components.header.header import header

app.register_blueprint(header)

## Footer
from components.footer.footer import footer

app.register_blueprint(footer)


@app.route('/logOut')
def logOut():
    session.clear()
    session['logedin'] = False
    session['isMani'] = False
    session['firstName'] = ''
    session['email'] = ' '
    return redirect('/homepage')
