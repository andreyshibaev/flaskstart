from flask import Blueprint, request, url_for, redirect, render_template, flash
newapp = Blueprint('newapp', __name__, template_folder="templates/newapp")

@newapp.route("/")
def home():
    return render_template('home.html')
