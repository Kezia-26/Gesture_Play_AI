# app.py

from flask import Flask, render_template, request, redirect, url_for, session
from auth import validate_user, register_user
import os
import subprocess

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if validate_user(email, password):
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid email or password.")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if register_user(email, password):
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template('signup.html', error="Email already exists.")
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# New Pages
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/technologies')
def technologies():
    return render_template('technologies.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Play Game Route
@app.route('/play/<game>')
def play_game(game):
    if 'user' not in session:
        return redirect(url_for('login'))

    if game == 'rps':
        subprocess.Popen(['python', 'gesture_rps.py'])
    elif game == 'tictactoe':
        subprocess.Popen(['python', 'gesture_tictactoe.py'])
    elif game == '2048':
        subprocess.Popen(['python', 'gesture_2048.py'])
    else:
        return "Invalid game selected."
    
    return f"<h2>Launching {game.capitalize()} game...<br>Close the game window to return.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
