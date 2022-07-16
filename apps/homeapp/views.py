from flask import Blueprint, request, url_for, redirect, render_template, flash
homeapp = Blueprint('homeapp', __name__, template_folder="templates/homeapp")
from apps.homeapp.models import Slider

@homeapp.route("/")
def home():
    slides = Slider.query.all()
    title = 'Главная страница'
    return render_template('home.html', title=title, slides=slides)
