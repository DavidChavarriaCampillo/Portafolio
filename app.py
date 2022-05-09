from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/principal")
def principal():
    return render_template("base.html")

@app.route("/integrante")
def integrante():
    return render_template("integrante.html")

app.run(debug=True)