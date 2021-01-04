from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts

#server object
app = Flask(__name__)

CORS(app)

#routes -> unique end points which server decides what to send to the view
@app.route('/',methods=['GET','POST'])

#function execute at end point
def index():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        #mehod for server to interact with the database
        create_post(name,post)

    posts = get_posts()

    return render_template('index.html',posts=posts)

if __name__=='__main__':
    app.run(debug=True)
