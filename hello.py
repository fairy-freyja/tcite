from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)
 
@app.route("/")
@app.route("/about")
def index():
    return render_template('index.html')
	
@app.route("/contact")
def contact():
	return render_template('contact.html')
	
@app.route("/conserts")
def conserts():
	return render_template('conserts.html')
	
@app.route("/listen")
def listen():
	return render_template('listen.html')
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)