
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    blog = TextAreaField('Write a blog')
    submit = SubmitField('Submit')

class BlogCommentForm(FlaskForm):
    blogcomment = TextAreaField('Comment on blog ')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Who are you.',validators = [Required()])
    submit = SubmitField('Submit')
