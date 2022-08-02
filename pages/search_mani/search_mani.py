from classes.searches import Search
from classes.manicurists import manicurist
from flask import Blueprint, render_template, session, jsonify, request, redirect

# sign_in blueprint definition
search_mani = Blueprint('search_mani', __name__, static_folder='static', static_url_path='/search_mani',
                        template_folder='templates')


# Routes

@search_mani.route('/search_mani')
def def_search_mani():
    if session['logedin'] == False:
        return render_template('searchAccessMess.html')
    if session['isMani'] == True:
        return render_template('noProfileMassageMani.html')

    return render_template('search_mani.html')


@search_mani.route('/search_mani_validation', methods=['post'])
def def_search_mani_validation():
    X_location = request.form['Latitude']
    Y_location = request.form['Longitude']
    maxPrice = request.form['pricerange']
    clientEmail = session['email']
    newSearch = Search(clientEmail, X_location, Y_location, maxPrice)
    isExist = newSearch.add_search()
    list = newSearch.find_mani()
    list = newSearch.find_mani()
    print(list)
    images = newSearch.imeges()
    print(images)
    message = newSearch.GetFind()
    if (message == 1):
        message="mani"
        return render_template('mani_results.html',
                               X_location=X_location, Y_location=Y_location,
                               maxPrice=maxPrice, list=list, images=images, message=message)
    return render_template('mani_results.html',
                           X_location=X_location, Y_location=Y_location,
                           maxPrice=maxPrice, list=list, images=images)
