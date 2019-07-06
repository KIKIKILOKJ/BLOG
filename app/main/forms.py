from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    blog = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')