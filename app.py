from flask import Flask, render_template
from jinja2 import Undefined

app = Flask(__name__)

inte = Undefined

@app.route("/")
@app.route("/principal")
def principal():
    return render_template("base.html")

@app.route("/david")
def david():
    return render_template("david.html")

@app.route("/duvan")
def duvan():
    return render_template("duvan.html")

app.run(debug=True)