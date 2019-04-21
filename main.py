from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:bobthebuilder@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'Hw3Gwfcv4'

db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    content = db.Column(db.String(1000))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Post %r>' % self.title

@app.route('/blogs')
def get_blogs():

    #blogs = Blog.query.filter_by(title=session['title']).all()

    return render_template('blogs.html')

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
        
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        #blog_id = int(request.form['blog-id'])
        #blog = Blog.query.get(blog_id)
        new_blog = Blog(title, content)
        db.session.add(new_blog)
        db.session.commit()
        return redirect('/blogs')
    else:
        return render_template('newpost.html')

if __name__ == "__main__":
    app.run()