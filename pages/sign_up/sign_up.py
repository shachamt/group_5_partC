from classes.customers import Customer
from flask import Blueprint, render_template, session, jsonify, request, redirect
import mysql.connector, requests
import os
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from classes.images import Image
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

    geolocator = Nominatim(user_agent="plzwork")
    location = geolocator.reverse(f"{x_location},{y_location}", language='en', )
    city=location.raw['address']['city']

    businessName = request.form['businessName']
    pic1=request.form['picture1']
    pic2=request.form['picture2']
    pic3=request.form['picture3']
    pic4=request.form['picture4']
    loggedMani = manicurist(email, FirstName, LastName, PhoneNumber, password, businessName, x_location, y_location,city)
    isExist = loggedMani.add_mani()
    if pic1.__eq__(pic2) |pic1.__eq__(pic3)|pic1.__eq__(pic4)|pic2.__eq__(pic3)|pic3.__eq__(pic4) | pic2.__eq__(pic4) :
        message="there is duplicate pictures please try again"
        return render_template('sign_up_mani.html', message=message)
    if (isExist):
        im1 = Image(pic1, email)
        im2 = Image(pic2, email)
        im3 = Image(pic3, email)
        im4 = Image(pic4, email)
        im1.addimage()
        im2.addimage()
        im3.addimage()
        im4.addimage()
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
