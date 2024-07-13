from flask import Flask, render_template, json, redirect, request, jsonify # py -m pip install flask
import os

app = Flask(__name__)

port = 2121

def extract_title_from_file(file_path):
    """
    Extracts the title from a Jinja file. This function assumes the title is set
    in a specific way, e.g., as a comment at the top of the file or a variable.
    Adjust the logic here based on how your titles are defined.
    """
    title = "Default Title"  # Default title in case extraction fails
    with open(file_path, 'r') as file:
        for line in file:
            # Example: Assuming the title is in a comment like '# Title: My Demo Title'
            if line.startswith('# Title:'):
                title = line.strip().split(':', 1)[1].strip()
                break
            # Add other conditions here if your title is defined differently
    return title

# create and return a dictionary of flask routes in this app with the file names they render organized into their respective directories

@ app.route('/')
def home():
    return render_template('/routes/index.j2')

@ app.route('/index') # this is the same as the home route but for the sake of the generator, it is included
def index():
    return render_template('/routes/index.j2')

@app.route('/projects')
def projects():
    projects = []
    # Construct an absolute path to the 'templates/routes/projects' directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    projects_dir = os.path.join(base_dir, 'templates', 'routes', 'projects')

    # Check if the directory exists
    if not os.path.exists(projects_dir):
        print(f"Directory does not exist: {projects_dir}")
        return "Projects directory not found.", 404
    
    # Iterate over the files in the directory
    for file in os.listdir(projects_dir):
        if file.endswith('.j2'):
            file_path = os.path.join(projects_dir, file)
            title = extract_title_from_file(file_path)
            projects.append({'name': file[:-3], 'title': title})
    return render_template('/routes/projects.j2', projects=projects)

@ app.route('/projects/<project>')
def project(project):

    return render_template(f'/routes/projects/{project}.j2')

@ app.route('/demos')
def demos():
    demos = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    demos_dir = os.path.join(base_dir, 'templates', 'routes', 'demos')

    if not os.path.exists(demos_dir):
        print(f"Directory does not exist: {demos_dir}")
        return "Demos directory not found.", 404
    
    for file in os.listdir(demos_dir):
        if file.endswith('.j2'):
            file_path = os.path.join(demos_dir, file)
            title = extract_title_from_file(file_path)
            demos.append({'name': file[:-3], 'title': title})
    return render_template('/routes/demos.j2', demos=demos)

@ app.route('/demos/<demo>')
def demo(demo):

    return render_template(f'/routes/demos/{demo}.j2')

@ app.route('/blog')
def blog():
    blog = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    blog_dir = os.path.join(base_dir, 'templates', 'routes', 'blog')

    if not os.path.exists(blog_dir):
        print(f"Directory does not exist: {blog_dir}")
        return "Blog directory not found.", 404
    
    for file in os.listdir(blog_dir):
        if file.endswith('.j2'):
            file_path = os.path.join(blog_dir, file)
            title = extract_title_from_file(file_path)
            blog.append({'name': file[:-3], 'title': title})
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