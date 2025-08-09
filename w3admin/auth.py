from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app as app
from flask_login import login_user
from flask_login import logout_user
from functools import wraps
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from .models import User
from . import db, mail

auth = Blueprint('auth', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def send_reset_email(user):
    token = get_reset_token(user)
    msg = Message('Restablecer Contraseña', 
                  sender='noreply@demo.com', 
                  recipients=[user.email])
    msg.body = f'''Para restablecer tu contraseña, visita el siguiente enlace:
{url_for('auth.reset_password', token=token, _external=True)}

Si no solicitaste este cambio, por favor ignora este correo.
'''
    mail.send(msg)

def get_reset_token(user, expires_sec=1800):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return s.dumps({'user_id': user.id}, salt=app.config['SECURITY_PASSWORD_SALT'])

def verify_reset_token(token):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token, salt=app.config['SECURITY_PASSWORD_SALT'], max_age=1800)['user_id']
    except Exception as e:
        print(f"Error al verificar el token: {e}")
        return None
    return User.query.get(user_id)

@auth.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            send_reset_email(user)
        flash('Si existe una cuenta con ese correo, se ha enviado un correo con las instrucciones para restablecer la contraseña.', 'info')
        return redirect(url_for('auth.forgot_password'))
    return render_template('w3admin/auth/forgot_password.html')

@auth.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = verify_reset_token(token)
    if user is None:
        flash('El token es inválido o ha expirado', 'warning')
        return redirect(url_for('auth.forgot_password'))
    if request.method == 'POST':
        password = request.form.get('password')
        if not password:
            flash('Por favor ingresa una contraseña', 'warning')
            return redirect(url_for('auth.reset_password', token=token))
        user.set_password(password)
        db.session.commit()
        flash('Tu contraseña ha sido actualizada', 'success')
        return redirect(url_for('auth.login'))
    return render_template('w3admin/auth/reset_password.html', token=token)



@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['dz-password']
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('auth.login'))
    return render_template('w3admin/auth/register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['dz-password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user, remember=True)  # 🔥 Esto gestiona la sesión con Flask-Login
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Correo o contraseña incorrectos', 'danger')
    return render_template('w3admin/auth/login.html')

@auth.route('/logout')
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente', 'success')
    return redirect(url_for('auth.login'))
