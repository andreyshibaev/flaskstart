from flask import Blueprint, render_template, redirect
from apps.contacts.forms import contactForm
contacts = Blueprint('contacts', __name__, template_folder='templates/contacts')



@contacts.route('/contacts', methods=['GET', 'POST'])
def show_contact_form():
    title = 'Форма связи'
    cform=contactForm()
    if cform.validate_on_submit():
        return redirect('/contacts')
    return render_template('contacts.html', title=title, cform=cform)