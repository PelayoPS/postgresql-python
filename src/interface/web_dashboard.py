from flask import Flask, render_template, request, redirect, url_for, flash, session
import src.data.database_setup as database_setup
from src.data.update_database import database_manager

app = Flask(__name__, template_folder='templates')
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    password = request.form['password']
    result, message = database_setup.setup(user, password)
    if not result:
        flash(message, 'error')
        return redirect(url_for('index'))
    flash(message, 'success')
    session['user'] = user
    session['password'] = password
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    user = session.get('user')
    password = session.get('password')
    if not user or not password:
        return redirect(url_for('index'))
    
    db_manager = database_manager(user, password)
    success, message = db_manager.create_table()
    if not success:
        flash(message, 'error')
        return redirect(url_for('index'))
    
    # Mostrar el dashboard con el nombre de la base de datos
    return render_template('dashboard.html', db_name='productividad')

if __name__ == "__main__":
    app.run(debug=True)
