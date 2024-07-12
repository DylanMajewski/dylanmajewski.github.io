from flask import Flask, render_template, json, redirect, request, jsonify # py -m pip install flask
import os

app = Flask(__name__)

port = 2121

# create and return a dictionary of flask routes in this app with the file names they render organized into their respective directories

@ app.route('/')
def home():
    return render_template('/routes/index.j2')

@ app.route('/index') # this is the same as the home route but for the sake of the generator, it is included
def index():
    return render_template('/routes/index.j2')

@ app.route('/projects')
def projects():
    projects = []
    for file in os.listdir(f'templates/routes/projects'):
        if file.endswith('.j2'):
            projects.append(file[:-3])
    return render_template('/routes/projects.j2', projects=projects)

@ app.route('/projects/<project>')
def project(project):

    return render_template(f'/routes/projects/{project}.j2')

@ app.route('/demos')
def demos():
    demos = []
    for file in os.listdir(f'templates/routes/demos'):
        if file.endswith('.j2'):
            demos.append(file[:-3])
    return render_template('/routes/demos.j2', demos=demos)

@ app.route('/demos/<demo>')
def demo(demo):

    return render_template(f'/routes/demos/{demo}.j2')

@ app.route('/blog')
def blog():
    blog = []
    for file in os.listdir(f'templates/routes/blog'):
        if file.endswith('.j2'):
            blog.append(file[:-3])
    return render_template('/routes/blog.j2', blog=blog)

@ app.route('/blog/<entry>')
def entry(entry):

    return render_template(f'/routes/entry/{entry}.j2')

@ app.route('/about')
def about():
    return render_template('/routes/about.j2')

@ app.route('/unfinished-page')
def under_construction():
    return render_template('/routes/unfinished-page.j2')

# if route does not exist, return a 404 page
@ app.errorhandler(404)
def page_not_found(e):
    return render_template('/routes/error.j2')

if __name__ == "__main__":

    # Start the app on port 2121, it will be different once hosted
    app.run(port=port, host='localhost', debug=True)