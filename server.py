from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")
    zipcode = request.form.get("zipcode")

    user = crud.create_user(fname, lname, email, password, zipcode)
 
    db.session.add(user)
    db.session.commit()
    flash("Account created! Please log in.")

    return redirect("/")




 
if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)