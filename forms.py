from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField
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
            validators.length(min=4, max=10, message="Ingrese nombre valido"),
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
