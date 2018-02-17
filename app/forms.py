
from wtforms import StringField, Form, TextAreaField
from wtforms.validators import DataRequired


class Contact(Form):
	name = StringField('Name', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	subject = StringField('Subject', validators=[DataRequired()])
	message = TextAreaField('Message', validators=[DataRequired()])