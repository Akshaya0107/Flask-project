from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Temporary in-memory user "database"
users_db = {}

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users_db and check_password_hash(users_db[username], password):
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")



@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users_db:
            return render_template("signup.html", error="Username already exists")

        users_db[username] = generate_password_hash(password)
        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

# ---------------- QUOTATION ----------------
@app.route('/quotation')
def quotation():
    return render_template("quotation.html")


# ---------------- INVOICE ----------------
@app.route('/invoice/tax')
def tax_invoice():
    return render_template("tax_invoice.html")

@app.route('/invoice/proforma')
def proforma_invoice():
    return render_template("proforma_invoice.html")


# ---------------- NOTES ----------------
@app.route('/note/credit')
def credit_note():
    return render_template("credit_note.html")

@app.route('/note/debit')
def debit_note():
    return render_template("debit_note.html")


# ---------------- VOUCHERS ----------------
@app.route('/voucher/receipt')
def receipt_voucher():
    return render_template("receipt_voucher.html")

@app.route('/voucher/payment')
def payment_voucher():
    return render_template("payment_voucher.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
