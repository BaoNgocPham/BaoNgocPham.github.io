from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

#set up app for flask
#export FLASK_APP=hello.py
#command ctril G : thay đổi link hay update những cái giống nhau cùng 1 lúc
# pip3 freeze > requirements.txt to make the requirement list to run this web


@app.route("/") #username part will make a dynamic website for any name you put behind /
def home():
    # {url_for('static', filename = 'favicon.ico')} #chua hoat dong, van load tu index
    """ do not need to hard embbed link below to html
     <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}"> """
    ""
    return render_template("./index.html")

@app.route("/<pagename>")
def html_page(pagename):
    return render_template(pagename)

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n {email}, {subject}, {message}")

def write_to_csv(data): #CSV stand for comma separated values
    with open("database.csv", newline="", mode="a") as database2: #cho newline vao truoc mode
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv.writer = csv.writer(database2, delimiter = ",", quotechar = ";", quoting = csv.QUOTE_MINIMAL) #default phai hoc thuoc
        csv.writer.writerow([email, subject, message])
        #writer.writerow() takes exactly one argument (3 given) so put them in list []

@app.route("/submit_form", methods = ["POST", "GET"]) #chu method phai co s, la methods, neu khong se error.
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict() #method to_dict to grab data
        write_to_csv(data)
        return "Your form has been submitted, we will comeback as soon as possible"
    #can return like this: return redirect("/thankyou.html)
    else:
        return "sth went wrong"




# @app.route("/index.html")
# def home2():
#     return render_template("./index.html")
#
# @app.route("/works.html")
# def works():
#     return render_template("./works.html")
#
# @app.route("/about.html")
# def about():
#     return render_template("./about.html")
#
#
# @app.route("/contact.html")
# def contact():
#     return render_template("./contact.html")
#
#
# @app.route("/blog")
# def blog():
#     return "Hello, welcome to my blog"



