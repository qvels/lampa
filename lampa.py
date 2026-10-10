from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Эта строка говорит Python: "Когда заходят на главную страницу, покажи index.html из папки templates"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)