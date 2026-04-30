from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my DevOps Project!"

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello, {name}!"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
@app.route("/about")
def about():
    return "This is the about page."
