from flask import Flask, request, render_template


# I lost my dawg,
# Csináltam új branchet
app = Flask(__name__)

@app.route('/login', methods=["POST"], strict_slashes=False)
def login():
    return{"login"}

@app.route('/register', methods=["POST"], strict_slashes=False)
def login():
    return{"regi"}