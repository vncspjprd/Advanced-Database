from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def register():
    return render_template("register.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        lastname = request.form["lastname"]
        firstname = request.form["firstname"]
        sex = request.form["sex"]
        institution = request.form["institution"]
        email = request.form["email"]
        return render_template(
            "details.html",
            lastname=lastname,
            firstname=firstname,
            sex=sex,
            institution=institution,
            email=email
        )
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)