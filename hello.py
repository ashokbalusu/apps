from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "test" # don't store this on GitHub. Keep this in Secrets

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"

def index():
    return render_template("index.html")

## Filters
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags

# localhost:8000/user/ashok
@app.route('/user/<name>')

# def user(name):
#     return "<h1>Hello {}!</h1>".format(name)
def user(name):
    return render_template("user.html"
                           , user_name=name)

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Create Name Page
@app.route('/name', methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()

    # Validate Form
    # if form.validate_on_submit():
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully")

    return render_template('name.html',
                           par_name = name,
                           par_form = form)
                           
if __name__ == '__main__':
    app.run(debug=True, port=8000)
