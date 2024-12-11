from flask import Flask, render_template, request, redirect, url_for, flash, session
import src.data.database_setup as database_setup
from src.data.update_database import database_manager
import pandas as pd

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
    
    show_placeholders = request.args.get('show_placeholders') == 'true'
    action = request.args.get('action')
    
    # Cargar datos de ejemplo
    data = pd.read_csv('src\\data\\database\\tareas.csv', delimiter=';', header=None).values.tolist()
    
    # Mostrar el dashboard con el nombre de la base de datos y placeholders si se solicitan
    return render_template('dashboard.html', db_name='productividad', show_placeholders=show_placeholders, data=data, action=action)

@app.route('/update_data', methods=['POST'])
def update_data():
    user = session.get('user')
    password = session.get('password')
    if not user or not password:
        return redirect(url_for('index'))
    
    column_name = request.form['column_name']
    value = request.form['value']
    condition = request.form['condition']
    
    db_manager = database_manager(user, password)
    success, message = db_manager.update_to_table('tareas', column_name, value, condition)
    if not success:
        flash(message, 'error')
    else:
        flash(message, 'success')
    
    return redirect(url_for('dashboard', action='update'))

@app.route('/insert_data', methods=['POST'])
def insert_data():
    user = session.get('user')
    password = session.get('password')
    if not user or not password:
        return redirect(url_for('index'))
    
    nombre = request.form['nombre']
    tareas = request.form['tareas']
    tareas_completadas = request.form['tareas_completadas']
    dia = request.form['dia']
    
    db_manager = database_manager(user, password)
    values = (nombre, tareas, tareas_completadas, dia)
    success, message = db_manager.insert_into_table('tareas', values)
    if not success:
        flash(message, 'error')
    else:
        flash(message, 'success')
    
    return redirect(url_for('dashboard', action='insert'))

@app.route('/delete_data', methods=['POST'])
def delete_data():
    user = session.get('user')
    password = session.get('password')
    if not user or not password:
        return redirect(url_for('index'))
    
    condition = request.form['delete_condition']
    
    db_manager = database_manager(user, password)
    success, message = db_manager.delete_from_table('tareas', condition)
    if not success:
        flash(message, 'error')
    else:
        flash(message, 'success')
    
    return redirect(url_for('dashboard', action='delete'))

if __name__ == "__main__":
    app.run(debug=True)
