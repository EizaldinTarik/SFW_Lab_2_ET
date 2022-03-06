from flask import Flask, render_template, request

# TODO: create new Flask app
app = Flask(__name__, static_folder = 'static')
global users
users=[]
@app.route("/")
def main_page():
    # TODO: return index.html
    return render_template("index.html")

@app.route("/sign_up",methods = ['POST'])
# TODO: Add route for sign up
def sign_up():
    # TODO: get user input from request
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']

    if not user_exists(email=email, username=username, password=password):
        return "<h2>Welcome, user has been created</h2>"
    else:
        return "<h2>Error! This user already exists</h2>"


def user_exists(email, username, password):
    # TODO: check for user if exists, you can use an array as your records.
    global users
    if username in users:
        return True
    else:
        users.append(username)
        return False
