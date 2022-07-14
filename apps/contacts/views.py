from flask import Blueprint, render_template, redirect, request, flash, url_for
from apps.contacts.forms import ContactForm
contacts = Blueprint('contacts', __name__, template_folder='templates/contacts')


from flask_mail import Message, Mail
mail = Mail()

@contacts.route('/contacts', methods=['GET', 'POST'])
def show_contact_form():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('Все поля обязательны!')
			return render_template('contacts.html', form=form)
		else:
			msg = Message(form.subject.data, sender='webmaster@sibchar.ru', recipients=['webmaster@sibchar.ru'])
			msg.body = """От: %s\n%s\nТекст сообщения:\n%s"""%(form.name.data, form.email.data, form.message.data)
			mail.send(msg)
			return redirect(url_for('contacts.show_contact_form'))
	return render_template('contacts.html', form=form, success=True)
