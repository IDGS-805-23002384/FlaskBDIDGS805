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
    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.length(min=4, max=10, message="Ingrese nombre valido"),
        ],
    )
    apaterno = StringField(
        "Apellido",
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
