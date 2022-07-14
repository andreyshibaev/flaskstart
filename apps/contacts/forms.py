from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms import ValidationError, validators

class ContactForm(FlaskForm):
	name = StringField("Имя",  [validators.InputRequired(message='Пожалуйста введите имя!')])
	email = StringField("Почта", [validators.Email(message='Пожалуйста введите почту!')])
	subject = StringField("Тема", [validators.InputRequired(message='Напишите тему сообщения!')])
	message = TextAreaField("Сообщение", [validators.InputRequired(message='Оставьте своё сообщение!')])
	submit = SubmitField("Отправить")