from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Website content goes here"

if name == "__main__":
    app.run(debug=True)
