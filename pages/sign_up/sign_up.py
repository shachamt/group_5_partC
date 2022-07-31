from classes.customers import Customer
from flask import Blueprint, render_template, session, jsonify, request, redirect
import mysql.connector, requests
import os
from dotenv import load_dotenv

from classes.manicurists import manicurist

sign_up = Blueprint('sign_up', __name__, static_folder='static', static_url_path='/sign_up',
                    template_folder='templates')


# DB



# Routes
@sign_up.route('/sign_up_customer')
def def_sign_up_page():
    if session['logedin'] == True:
        return render_template('signInMessage.html')
    return render_template('sign_up_customer.html')


@sign_up.route('/commit_sign_up', methods=['POST', 'GET'])
def def_sign_up_customer():
    email = request.form['email']
    FirstName = request.form['firstName']
    LastName = request.form['lastName']
    PhoneNumber = request.form['telephone']
    password = request.form['password']
    loggedCustomer = Customer(email, FirstName, LastName, PhoneNumber, password)
    isExist = loggedCustomer.add_customer()
    if (isExist):
        session['email'] = email
        session['firstName'] = loggedCustomer.getFirstName()
        session['lastName'] = loggedCustomer.getLastName()
        session['phoneNumber'] = loggedCustomer.getPhoneNumber()
        session['logedin'] = True
        session['isMani'] = False
        return render_template('homepage.html')
    return render_template('sign_up_customer.html', message='username already exist')


@sign_up.route('/sign_up_mani')
def def_sign_up_mani_page():
    if session['logedin'] == True:
        return render_template('signInMessage.html')
    return render_template('sign_up_mani.html')


@sign_up.route('/commit_sign_up_mani', methods=['POST', 'GET'])
def def_sign_up_mani():
    email = request.form['email']
    FirstName = request.form['firstName']
    LastName = request.form['lastName']
    PhoneNumber = request.form['telephone']
    password = request.form['password']
    x_location = request.form['Latitude']
    y_location = request.form['Longitude']
    businessName = request.form['businessName']
    loggedMani = manicurist(email, FirstName, LastName, PhoneNumber, password, businessName, x_location, y_location)
    isExist = loggedMani.add_mani()
    if (isExist):
        session['email'] = email
        session['logedin'] = True
        session['isMani'] = True
        session['firstName'] = loggedMani.getFirstName()
        session['lastName'] = loggedMani.getLastName()
        session['phoneNumber'] = loggedMani.getPhoneNumber()
        session['businessName'] = loggedMani.getBusinessName()
        session['x'] = loggedMani.getXLocation()
        session['y'] = loggedMani.getYLocation()
        session['aboutMe'] = loggedMani.getAbout()
        session['rate'] = loggedMani.getTotalRate()

        return redirect('/homepage')
    return render_template('sign_up_mani.html', message='username already exist')
