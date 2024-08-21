"""auth's routes"""
from flask import render_template, redirect, url_for, request, flash
from app.auth import bp

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Maneja las solicitudes de inicio de sesión.

    Métodos:
        GET: Muestra el formulario de inicio de sesión.
        POST: Procesa los datos del formulario de inicio de sesión.

    Returns:
        str: La plantilla de inicio de sesión o redirige a la página de inicio.
    """
    if request.method == 'POST':
        # Aquí iría la lógica para autenticar al usuario
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':  # Ejemplo simple
            return redirect(url_for('main.home'))
        else:
            flash('Nombre de usuario o contraseña incorrectos.', 'danger')

    return render_template('auth/login.html')
