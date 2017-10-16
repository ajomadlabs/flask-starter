'''
This is a basic Python Flask Web App
Main.py is the file which is called to run your web app.
'''
#Importing the Flask Module
from flask import Flask, request, render_template, redirect, url_for, session, flash

'''
Creating a Flask Object
'__name__' is passed to make the Flaks know that this is the root of the app.
When we help Flask to find the root, finding all other files will be a lot more easier. 
'''
app = Flask(__name__)
app.secret_key = "Secret Key"

'''
Now we need to define the different routes.
Routes basically means the path to different pages.
'/' this indicates the root or the home page of the website
'/about' this indicates the path to the about page
This basically ties a URL to a python function
'''

'''
Routing is the concept by which we add paths to different
web pages.
In Flask, routing is made possible with decorators.
Decorators are those which helps to wrap a function and 
modify its behaviour.
'@' is used to represent it.
Routing in simple words means connecting an URL to the
return value of that function.
'''
#Defining route of home page
@app.route('/')
def index():
    return 'This is the home page. Thank you !'

#Definig the route of about page
@app.route('/about')
def about():
    return '<h2>About Us</h2>'

#Defining the route of welcome page
@app.route('/welcome')
def welcome():
    return '<h2>Welcome ! Nice to have you</h2>'
'''
Passing values through URL and changing
page content according to the values
'''
#Defining the route of profile page
@app.route('/profile/<username>')
def profile(username):
    return '<h2>Hey there %s</h2>' %username

'''
If you need to pass integer values via URL
you need to specify the datatype
'''
#Defining the route for newsfeed
@app.route('/news/<int:newsid>')
def news(newsid):
    return '<h2>News Id : %s</h2>' %newsid

'''
The next concept is about Http Requests.
Everything in the web is communicated via requests.
By default all the request is GET.
If you need to submit confidential data like forms
we need to make use of POST.
For this we import the request module.
'''
#Defining the route for GET request
@app.route('/getrequest')
def getrequest():
    return '<h2>Request Type : %s</h2>'%request.method 

#Defining the route for POST request
@app.route('/postrequest', methods=['GET', 'POST'])
def postrequest():
    if request.method == 'POST':
        return '<h2>Request Method : %s</h2>'% request.method
    else:
        return '<h2>Request Method : %s</h2>'%request.method

'''
Now the above are all just demos on how to get your hands 
dirty with Flask. 
When you actually start your project, you have to orgainze 
your files.
In this above code you may have seen that I returned using 
HTML tags which is not a nice way to do so.
So to organize all of this, we create another directory
called templates. Templates will consists of the HTML files.
For this we import another module called 'render_template'
We also create another directory called Static. This contain
all of our CSS and Javascript files for the project.
'''
#Definig the route for profile using templates
@app.route('/tprofile/<username>')
def tprofile(username):
    return render_template("tprofile.html", username=username)

'''
On rendering and going to this route we see it working
But now we need to give some styles and that's where 
we need to have CSS.
'''

'''
Mapping Different URL's to the same function.
The usecase is when we need to show two different
content based on the URL.
'''

#Defining the route for user using templates
@app.route('/user')
@app.route('/user/<username>')
def user(username=None):
    return render_template("user.html", username=username)

'''
Now at last we are going to see how to
display a list of objects.
'''
#Defining the route for userslist
@app.route('/userslist')
def userlist():
    users = ['Bobin', 'Megha', 'Arshit', 'Seira']
    return render_template("userslist.html", users=users)

'''
Now we will move on to how to submit forms
using Flask - Basically a Login and SignUp
form.
'''
#Defining the route for login 
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = "Invalid username and password"
        else:
            session['logged_in'] = True
            flash("You were Logged In")
            return redirect(url_for('welcome'))
    return render_template("login.html", error=error)

#Defining the route of logout
@app.route('/logout')
def logout():
    session.pop['logged_in', None]
    flash("You were just Logged out")
    return redirect(url_for('about'))

#Starts the app running
if __name__ == "__main__":
    app.run(debug=True)