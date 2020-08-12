from Phone_book import app
from flask import render_template, request

# Import for Forms
from Phone_book.forms import UserInfoForm, BlogPostForm

# home route
@app.route('/')
def home():
    item_dict = {1: "IronMan", 2: "Thor", 3:"Hulk", 4:"Thanos"}
    return render_template("home.html", item_dict=item_dict)

