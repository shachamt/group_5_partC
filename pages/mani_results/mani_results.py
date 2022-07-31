from flask import Blueprint, render_template, redirect, url_for
# sign_in blueprint definition
mani_results = Blueprint('mani_results', __name__, static_folder='static', static_url_path='/mani_results', template_folder='templates')


# Routes

@mani_results.route('/mani_results')
def def_mani_results():
    return render_template('mani_results.html')