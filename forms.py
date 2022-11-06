from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class QueryIdForm(Form):
	'''
	Form to perform the search functionality
	in the /search route where one needs to
	type in the first and last name
	'''
	query_id = TextField('Enter Query ID', validators=[validators.DataRequired()])