from flask import Blueprint, render_template, session, jsonify, request, redirect
import mysql.connector, requests
import os
from dotenv import load_dotenv  # sign_in blueprint definition


from classes.signIn import signIn
from classes.manicurists import manicurist
from classes.customers import Customer



sign_in = Blueprint('sign_in', __name__, static_folder='static', static_url_path='/sign_in',
                    template_folder='templates')


# Routes
@sign_in.route('/sign_in', methods=['GET', 'POST'])
def def_sign_in_page():
    if session['logedin']==True:
        return render_template('signInMessage.html')
    return render_template('sign_in.html')


@sign_in.route('/after_click_sign_in', methods=['GET', 'POST'])
def def_sign_in():
    email = request.form['email']
    password = request.form['password']
    newSign= signIn(email, password)
    isExist = newSign.ex_username()
    if isExist == 0: #exist and correct password
        session['logedin'] = True
        if newSign.isMani()==True: #manicurist
            session['isMani'] = True
            loggedMani=manicurist(email=email,FirstName='',LastName='',PhoneNumber='',password='',businessName='',x_location='',y_location='')
            session['email'] = email
            session['firstName'] = loggedMani.getFirstName()
            session['lastName'] = loggedMani.getLastName()
            session['phoneNumber'] = loggedMani.getPhoneNumber()
            session['businessName'] = loggedMani.getBusinessName()
            session['x'] = loggedMani.getXLocation()
            session['y'] = loggedMani.getYLocation()
            session['aboutMe'] = loggedMani.getAbout()
            session['rate'] = loggedMani.getTotalRate()

        else: #customer
            loggedCustomer=Customer(Email=email,FirstName='',LastName='',phoneNumber='',password='')
            session['email'] = email
            session['firstName'] = loggedCustomer.getFirstName()
            session['lastName'] = loggedCustomer.getLastName()
            session['phoneNumber'] = loggedCustomer.getPhoneNumber()
            session['isMani'] = False

        return redirect('/homepage')
    elif isExist == 1: #exist with wrong password
        return render_template('sign_in.html', message="wrong password - please try again")
    return render_template('sign_in.html', message="you did not registered - please sign up")
    #doesnt exist
