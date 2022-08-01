from flask import Blueprint, render_template, redirect, url_for, session, request

# sign_in blueprint definition
business_profile = Blueprint('business_profile', __name__, static_folder='static', static_url_path='/business_profile',
                             template_folder='templates')
from utilities.db.db_manager import dbManager
from utilities.db.db_manager import dbManager
from classes.manicurists import manicurist
from classes.dynamicMani import DynamicMani
from classes.ratings import Rate




# Routes

@business_profile.route('/business_profile')
def def_business_profile():
    if session['isMani'] == False:
        return render_template('noProfileMessage.html')
    email= session['email']
    newManicurist= manicurist(email,FirstName='',LastName='',PhoneNumber='',password='',businessName='',x_location='',y_location='')
    users_list = newManicurist.getServices()
    manicurists = newManicurist.getMyDetails()
    images = newManicurist.getMyImages()

    return render_template('business_profile.html', services=users_list, name=manicurists[0][1],
                           aboutMe=manicurists[0][8], images=images,rate=manicurists[0][9], ismani= session['isMani'])


@business_profile.route('/business_profile/<int:ID>')
def def_business_profile_ByID(ID):
    newDynamic= DynamicMani(ID)
    email = newDynamic.getEmail() #email of manicurist
    if email== 'null':
        return render_template('IDnotFound.html')
    print(email)
    session['currentMani']=email[0]
    newManicurist= manicurist(email,FirstName='',LastName='',PhoneNumber='',password='',businessName='',x_location='',y_location='')
    users_list = newManicurist.getServices()
    manicurists = newManicurist.getMyDetails()
    images = newManicurist.getMyImages()
    if session['isMani'] == True:
        return render_template('noProfileMessage.html')
    return render_template('business_profile.html', services=users_list, name=manicurists[0][1],
                           aboutMe=manicurists[0][8], images=images,rate=manicurists[0][9], ismani= session['isMani'])


@business_profile.route('/business_edit')
def def_business_edit():
    email = session['email']
    newManicurist = manicurist(email, FirstName='', LastName='', PhoneNumber='', password='', businessName='',
                               x_location='', y_location='')
    users_list = newManicurist.getServices()
    manicurists = newManicurist.getMyDetails()
    images = newManicurist.getMyImages()
    return render_template('business_edit.html', services=users_list, name=manicurists[0][1],
                           aboutMe=manicurists[0][8], images=images,rate=manicurists[0][9], ismani= session['isMani'])


@business_profile.route('/business_edit_about', methods=['get', 'post'])
def def_business_edit_AboutMe():
    email = session['email']
    newAbout = request.form['feedText']
    newManicurist = manicurist(email, FirstName='', LastName='', PhoneNumber='', password='', businessName='',
                               x_location='', y_location='')
    users_list = newManicurist.getServices()
    manicurists = newManicurist.getMyDetails()
    images = newManicurist.getMyImages()
    if newAbout != '':
        newManicurist.setAbout(newAbout)
        message = "description successfully updated"
    else:
        message = "description is empty - please fill before submitting"
    return render_template('business_edit.html', services=users_list, name=manicurists[0][1],
                           aboutMe=manicurists[0][8], images=images, message=message,rate=manicurists[0][9], ismani= session['isMani'])


@business_profile.route('/business_edit_service/<line>', methods=['get', 'post'])
def def_business_edit_service(line):
    duplicate=False
    email = session['email']
    service = "service" + line
    current = "currentService" + line
    price = "price" + line
    newCurrent = request.form[current]
    newService = request.form[service]
    newPrice = request.form[price]
    newManicurist = manicurist(email, FirstName='', LastName='', PhoneNumber='', password='', businessName='',
                               x_location='', y_location='')
    currentServices = newManicurist.getServices()
    for service in currentServices:
        if service.serviceName == newService:
            duplicate = True
    if newService != '':
        if newPrice == '':
            if duplicate == False: #update new service
                newManicurist.updateServiceName(newService, email, newCurrent)
                message = "service name successfully updated"
            else:
                message = "service name already exist"
    if newService == '':
        if newPrice != '':
            newManicurist.updateServicePrice(newPrice, email, newCurrent)
            message = "service price successfully updated"
    if newService != '':
        if newPrice != '':
            if duplicate == False:
                newManicurist.updateNamePrice(newService, newPrice, email, newCurrent)
                message = "service successfully updated"
            else:
                message = "service name already exist"
    currentServices = newManicurist.getServices()
    manicurists = newManicurist.getMyDetails()
    images = newManicurist.getMyImages()
    return render_template('business_edit.html', services=currentServices, name=manicurists[0][1],
                           aboutMe=manicurists[0][8], images=images, message=message,rate=manicurists[0][9], ismani= session['isMani'])

@business_profile.route('/rating')
def def_rating():
    newrate = request.args['Rate']
    email=session['email']
    s= Rate(session['currentMani'],email,newrate)
    s.add_rate()
    return redirect('/homepage')
