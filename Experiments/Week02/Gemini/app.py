import re
from flask import Flask, render_template, request

# Initialize the Flask app FIRST
app = Flask(__name__)

# Simple standard-library email validation pattern
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

def validate_contact_form(data):
    errors = {}
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not name:
        errors["name"] = "Name is required."

    if not email:
        errors["email"] = "Email is required."
    elif not EMAIL_REGEX.match(email):
        errors["email"] = "Please enter a valid email address."

    if not message:
        errors["message"] = "Message is required."

    return errors

# Routes come AFTER 'app' is initialized
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form_data = {
            "name": request.form.get("name", ""),
            "email": request.form.get("email", ""),
            "message": request.form.get("message", "")
        }
        
        errors = validate_contact_form(form_data)
        if errors:
            return render_template("contact.html", errors=errors, form_data=form_data), 400
        
        return render_template("contact_success.html")

    return render_template("contact.html", errors={}, form_data={})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
