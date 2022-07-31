from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
header = Blueprint('header', __name__, static_folder='static', static_url_path='/header', template_folder='templates')

