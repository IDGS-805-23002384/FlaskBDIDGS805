from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField, SelectField, TextAreaField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    id = IntegerField(
        "Id",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.NumberRange(min=100, max=1000, message="Ingrese valor válido"),
        ],
    )
    matricula = IntegerField(
        "matricula",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.NumberRange(min=100, max=1000, message="Ingrese valor válido"),
        ],
    )
    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.length(min=3, max=200, message="Ingrese nombre valido"),
        ],
    )
    apellidos = StringField(
        "Apellidos",
        [
            validators.DataRequired(message="El campo es requerido"),
        ],
    )
    # amaterno=StringField("amaterno",[
    #     validators.DataRequired(message="El campo es requerido"),

    # ])
    email = EmailField(
        "Correo",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.Email(message="Ingresa correo valido"),
        ],
    )
    telefono = StringField(
        "Teléfono",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.Email(message="Ingresa correo valido"),
        ],
    )
    especialidad = StringField(
        "Especialidad",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.DataRequired(message="Ingresa correo valido"),
        ],
    )


class CursoForm(Form):
    id = IntegerField("Id")
    nombre = StringField(
        "Nombre del Curso",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.length(min=3, max=150, message="Ingrese nombre válido"),
        ],
    )
    descripcion = TextAreaField(
        "Descripción",
        [
            validators.DataRequired(message="El campo es requerido"),
        ],
    )
    maestro_id = SelectField(
        "Maestro",
        [
            validators.DataRequired(message="Selecciona un maestro"),
        ],
        coerce=int,
    )


class InscripcionForm(Form):
    alumno_id = SelectField(
        "Alumno",
        [
            validators.DataRequired(message="Selecciona un alumno"),
        ],
        coerce=int,
    )
    curso_id = SelectField(
        "Curso",
        [
            validators.DataRequired(message="Selecciona un curso"),
        ],
        coerce=int,
    )
