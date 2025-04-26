# Oh no! This site is broken. 
# Look for TODO comments and fill the 
# underline placeholders with the correct code

import requests
from flask import Flask, session, render_template, request, redirect, url_for
from cs50 import SQL
import bcrypt
import base64
import hashlib

# TODO 1: initialize SQLite for this app with the db name of user.db
# Follow the 'https://cs50.readthedocs.io/libraries/cs50/python/' docs and look for sqlite `SQL` method
# db = SQL("sqlite:///___")
db = SQL("sqlite:///user.db")

app = Flask(__name__)
# TODO 2: generate a strong secret key
# You can open a new terminal and copy+paste this code 
# python -c 'import secrets; print(secrets.token_hex())'
# Place the output as the value for app.secret_key
# We need the secret key to make our server-side session secure
app.secret_key = 'a6db69d39918a075534bf3850dabbd7d10514bbd7a5b8e93bc9a196fa91a6fd9'

@app.route('/')
def home():
    if 'user' in session:
        # Massive shoutout to MohammadReza Keikavousi for the fakestoreapi
        fake_store = requests.get("https://fakestoreapi.com/products?limit=20")
        
        return render_template('index.html', fake_store=fake_store.json())
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return "Missing email or password", 400 
        
        try:
            # TODO 3: use db.execute to get the user record referencing user's email, name this variable as user
            user = db.execute("SELECT * FROM user WHERE email=?", email)
            
            if len(user) != 1:
                return 'Invalid email', 400

            # Use bcrypt to check the password hash
            if bcrypt.checkpw(base64.b64encode(hashlib.sha256(password.encode('utf-8')).digest()), user[0]['password']):
                # set user session  
                session['user'] = {'email': user[0]['email'], 'username': user[0]['username']}
            else:
                return 'Invalid password', 400
            
            return redirect(url_for('home'))
        
        except:
            return 'Failed to login', 500
        
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user' in session:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')

        if not email or not password or not username:
            return "Missing email, username, or password", 400 
        
        try:
            # TODO 4: use db.execute to get the user record referencing user's email, name this variable as user
            user = db.execute('SELECT * FROM user WHERE email=? ', email)
            
            if user:
                return 'Email already exists', 400
            
            # Hash the password and store it in database
            hash = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password.encode('utf-8')).digest()), bcrypt.gensalt())

            # TODO 5: insert the email and hash to the database
            db.execute('INSERT INTO user(email, password, username) VALUES(?, ?, ?)', email, hash, username)

            # add user to session
            session['user'] = {'email': email, 'username': username}

            return redirect(url_for('home'))

        except:
            return 'Failed to signup', 500
        
    return render_template('signup.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/change-username', methods=['POST'])
def update_username():
    if 'user' not in session:
        return redirect(url_for('login'))

    username = request.form.get('username')

    if not username:
        return 'Failed change name', 400
    
    # TODO 6: update the username
    # db.execute('UPDATE ___ SET _____=? WHERE _____=?', ______, session['user']['email'])
    session['user']['username'] = username
    session.modified = True

    return redirect(url_for('settings'))


@app.route('/change-password', methods=['POST'])
def update_password():
    if 'user' not in session:
        return redirect(url_for('login'))

    password = request.form.get('password')

    if not password:
        return 'Failed change password', 400
    
    hash = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password.encode('utf-8')).digest()), bcrypt.gensalt())
    # TODO 7: update the password
    # db.execute('UPDATE ___ SET _____=? WHERE _____=?', _____, session['user']['email'])

    return redirect(url_for('settings'))


@app.route('/delete-account', methods=['POST'])
def delete_account():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    # TODO 8: update the username
    # db.execute('DELETE FROM _____ WHERE ____=?', session['user']['email'])
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login')) 

if __name__ == '__main__':
    app.run(debug=True, port=5000)