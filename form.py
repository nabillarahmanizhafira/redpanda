from wtforms import Form
from wtforms import StringField
from wtforms import SelectField
from wtforms import validators


class FeedbackForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    full_name = StringField('Full Name', [validators.DataRequired()])
    subject = StringField('Subject', [validators.DataRequired()])
    body = StringField('Body', [validators.Length(min=30)])