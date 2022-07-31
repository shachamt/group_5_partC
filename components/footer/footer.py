from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
footer = Blueprint('footer', __name__, static_folder='static', static_url_path='/footer', template_folder='templates')

