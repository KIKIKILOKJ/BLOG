from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class CommentForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    comment = TextAreaField('Blog comment', validators=[Required()])
    submit = SubmitField('Submit')