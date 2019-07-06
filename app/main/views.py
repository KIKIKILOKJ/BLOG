from flask import render_template,request,redirect,url_for,abort
from . import main
from ..forms import BlogForm
# Comment = comment.Comment
# from . import get_quotes

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    #Getting random quotes
    # random_quotes= get_quotes()
    # print(random_quotes)

    title = 'Home'

    return render_template('index.html', title = title) #random = random_quotes 

@main.route('/blog/new/<int:id>',methods = ['GET','POST'])
def comments(id):
    form = BlogForm()
    
    if form.validate_on_submit():
        name = form.name.data
        blog = Blog(name = name)
        # new_blog = Blog('')
        