
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app  = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY-ECHO']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:root@localhost:8889/build-a-blog'

db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(60))
    text = db.Column(db.String(300))

    def __init__ (self, subject, text):
        self.subject = subject
        self.text = text 
        

@app.route('/blog', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        new_subject = request.form.get('subject')
        new_text = request.form['text']
        list_blog = Blog(new_subject, new_text)

        db.session.add(list_blog)
        db.session.commit()

    
    blog = Blog.query.all()


    
    if request.args.get('id'):
        id = request.args.get('id')
        view = Blog.query.get(id)
        return render_template('viewBlog.html', pagetitle = view.subject, show_text = view.text )
    
    return render_template('blog.html', pagetitle = 'My Blog', blog = blog)


@app.route('/newpost', methods=['POST', 'GET'])
def newBlog():
    
     if request.method == 'POST':
        id = request.form.get('')
        

     return render_template('addBlog.html', pagetitle = "Add A New Blog")

@app.route('/view')
def viewBlog():
    id = request.args.get('id')
    #display_subject = Blog.query.filter_by(id = id).all()
    return str(id)
    


if __name__ == '__main__':
app.run()