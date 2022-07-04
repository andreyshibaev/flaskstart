from flask import Blueprint, request, url_for, redirect, render_template, flash
homeapp = Blueprint('homeapp', __name__, template_folder="templates/homeapp")

@homeapp.route("/")
def home():
    title = 'Home page'
    return render_template('home.html', title=title)
