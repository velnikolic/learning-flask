#import the flask class and the function render template
from flask import Flask, render_template

#new usable instance of Flask class
app = Flask(__name__)

#mapl the url "/" to the Python function index
@app.route("/")
#create index function
def index():
    #uses render_template function to return index.html
    return render_template("index.html")


#mapl the url "about" to the Python function about
@app.route("/about")
def about():
    #uses render_template function to return index.html
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
