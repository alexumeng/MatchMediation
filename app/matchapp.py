import ast
from flask import Flask, render_template, url_for, request, jsonify, redirect
app = Flask(__name__) #name of module

registered_users = 'users.txt'

logged_in_user_info = ""

search_filter = ""

search_query = ""

#what we type into our browser to go to different pages
@app.route("/") #home page
def welcome():
    return render_template('registration.html') #name of home html file --> will change as front end is developed

@app.route("/parent", methods =["GET", "POST"]) #parent sign up page
def parent():
    if request.method == "POST":
        global logged_in_user_info
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        password = request.form.get("password")
        email = request.form.get("email")
        phone = request.form.get("number").replace("-", "")

        open_dict ="\'{ "
        user_info = "\"fname\": \"{}\",\"lname\": \"{}\", \"password\": \"{}\", \"email\": \"{}\",\"phone\": \"{}\", \"acct_type\": \"parent\"".format(first_name, last_name, password, email, phone)
        closing_dict = "}\'\n"

        new_user = open_dict + user_info + closing_dict

        #print(new_user)

        file = open(registered_users, 'a+')
        file.write(new_user)
        file.seek(0)
        registered = file.readlines()
        file.close()

        # for users in registered:
        #     print(users.strip())
        logged_in_user_info = new_user
        return redirect("/home") #redirect to page after sign-up here


    return render_template('parent.html')

@app.route("/supervisor", methods =["GET", "POST"])
def supervisor():
    if request.method == "POST":
        global logged_in_user_info
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        password = request.form.get("password")
        email = request.form.get("email")
        phone = request.form.get("number").replace("-", "")

        open_dict ="\'{ "
        user_info = "\"fname\": \"{}\",\"lname\": \"{}\", \"password\": \"{}\", \"email\": \"{}\",\"phone\": \"{}\", \"acct_type\": \"supervisor\"".format(first_name, last_name, password, email, phone)
        closing_dict = "}\'\n"

        new_user = open_dict + user_info + closing_dict

        #print(new_user)

        file = open(registered_users, 'a+')
        file.write(new_user)
        file.seek(0)
        registered = file.readlines()
        file.close()

        file = open("supervisors.txt", 'a+')
        file.write(new_user)
        file.seek(0)
        file.close()

        # for users in registered:
        #     print(users.strip())
        print("supervisor 1st part added successfully")
        logged_in_user_info = new_user

        return redirect("/home") #redirect to page after sign-up here

    return render_template('supervisor.html')

@app.route("/login", methods =["GET", "POST"])
def login():
    if request.method == "POST":
        global logged_in_user_info
        email = request.form.get("email")
        password = request.form.get("password")

        file = open(registered_users, 'r')
        registered = file.readlines()

        exists = False
        for user in registered:
            if exists == True:
                file.close()
                break

            user = str(user)
            user_info = ast.literal_eval(user)

            if ast.literal_eval(user_info)["email"] == email:
                if ast.literal_eval(user_info)['password'] == password:
                    exists = True
                    logged_in_user_info = user

        file.close()
        if exists == False:
            print("login incorrect")
            return redirect("/login") #page to go to if login is incorrect

        print("login correct")

        return redirect("/home") #page to go to if login is successful

    return render_template("login.html")

''' all webpages under this comment are available after successful login'''

@app.route("/home", methods =["GET", "POST"])
def home():
    return render_template('index.html')

@app.route("/supervisors", methods =["GET", "POST"])
def supervisors():
    if request.method == "POST":
        file = open("supervisors.txt", "r")
        supers = file.openlines()
        file.close()

    return render_template('supervisors.html')

@app.route("/resources", methods =["GET", "POST"])
def resources():
    if request.method == "POST":
        global search_query
        search = request.form.get("search")


    return render_template('resources.html')

@app.route("/education", methods =["GET", "POST"])
def education():
    if request.method == "POST":
        global search_query
        search = request.form.get("search")
    return render_template('education.html')

@app.route("/custody", methods =["GET", "POST"])
def custody():
    if request.method == "POST":
        global search_query
        search = request.form.get("search")
    return render_template('custody.html')

@app.route("/laws", methods =["GET", "POST"])
def laws():
    if request.method == "POST":
        global search_query
        search = request.form.get("search")
    return render_template('laws.html')


if __name__ == '__main__':
    app.run(debug=True)