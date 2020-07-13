from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(min=2,max=30)], render_kw={"placeholder":"Nombre"})
    lastname = StringField(validators=[DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Apellido"})
    email = StringField(validators=[DataRequired(), Email()], render_kw={"placeholder": "Correo electrónico"})
    password = PasswordField(validators=[DataRequired(),Length(min=8,max=50)], render_kw={"placeholder": "Contraseña"})
    conf_pass = PasswordField(validators=[DataRequired(),
                             Length(min=8,max=50), EqualTo('password')], render_kw={"placeholder":"Confirme contraseña"})
    username = StringField(validators=[DataRequired(),Length(min=4,max=15)], render_kw={"placeholder": "Nombre de usuario"})
    submit = SubmitField('Crear cuenta')

class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()],
            render_kw={"placeholder": "Correo electrónico"} )
    password = PasswordField(validators=[DataRequired(),Length(min=8,max=50),
               EqualTo('password')], render_kw={"placeholder": "Contraseña"})
    submit = SubmitField('Iniciar sesión')
