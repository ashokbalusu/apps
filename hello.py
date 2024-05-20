from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=8000)
