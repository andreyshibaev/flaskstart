from flask import Blueprint, request, url_for, redirect, render_template, flash

profile = Blueprint('profile', __name__, template_folder="templates/profile")

@profile.route("/profile")
def profile_account():
    return render_template('profile.html')
