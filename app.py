from flask import Flask, render_template, request
import os 
import markdown

app = Flask(__name__)

essay_folder = "essays"

def list_essays():
    return [f[:-3] for f in os.listdir(essay_folder) if f.endswith(".md")]

def load_essay(filename):
    try:
        with open(os.path.join(essay_folder, filename + ".md"), "r", encoding="utf-8") as file:
            return markdown.markdown(file.read())
    except FileNotFoundError:
        return "<h2>Oops, I couldn't find the essay you're looking for. Please contact me if this issue persists.</h2>"

@app.route("/")
def home():
    essays = list_essays()
    return render_template("index.html", essays=essays)

@app.route("/essays/<name>")
def show_essay(name):
    content = load_essay(name)
    return render_template("essay.html", title=name.replace("_", " "), content=content)

if __name__ == "__main__":
    app.run(debug=True)
