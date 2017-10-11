from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home(): # Name of the method
    return render_template("index.html")

@app.route("/contact-me")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='80') #Run the flask app at port 4000
