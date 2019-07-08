from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Blog, BlogComment
from .. import db
from flask_login import login_required, current_user
from .forms import *
import markdown2


@main.route('/')
def index():

    return render_template('index.html')

@main.route('/blog', methods = ['GET','POST'])
@login_required
def blog():
    form = BlogForm()
    title = 'Blog pitches'
    if form.validate_on_submit():
        new_blog = Blog(blog=form.blog.data, user_id=current_user.id)

        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('.allblogs'))

    return render_template("blog.html", title = title, blogsform= form)


@main.route('/blog/<int:id>',  methods=['GET', 'POST'])
@login_required
def blog_id(id):

    blog = Blog.query.get(id)
    form = BlogCommentForm()
    if form.validate_on_submit():
        blogcomment = form.blogcomment.data
        new_blogcomment = BlogComment(blogcomment=blogcomment, blog_id=id, user=current_user)
        new_blogcomment.save_blogcomment()

    blogcomment = BlogComment.query.filter_by(blog_id=id).all()
    return render_template('blogies.html',blogform=form, blogcomments = blogcomment, blog=blog)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

