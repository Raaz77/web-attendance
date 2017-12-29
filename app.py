from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os
app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('indexx.html')
    else:
        return render_template("mainpage.html") + "<a href='/logout'>Logout</a>"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['pas'] == "password" and request.form['usernme'] == "admin":
        session['logged_in'] = True
        return home()
    else:
        
    	return home()
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
    



if __name__ == "__main__":
    
    app.run(debug=True,host='0.0.0.0', port=4000)
