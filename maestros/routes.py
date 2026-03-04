import forms
from . import maestros
from flask import render_template, request, redirect, url_for

from models import db, Maestros

# @maestros.route('/perfil/<nombre>')
# def perfil(nombre):
#     return f"Perfil de {nombre}"


@maestros.route("/maestros", methods=["GET", "POST"])
def lista_maestros():
    create_form = forms.UserForm(request.form)
    maestros = Maestros.query.all()
    return render_template(
        "maestros/listadoMest.html", form=create_form, maestros=maestros
    )


@maestros.route("/maestrosA", methods=["GET", "POST"])
def maestros_a():
    create_form = forms.UserForm(request.form)

    if request.method == "POST":
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            especialidad=create_form.especialidad.data,
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for("maestros.lista_maestros"))
    return render_template("maestros/maestros_a.html", form=create_form)


@maestros.route("/detalles_a", methods=["GET", "POST"])
def detalles_a():
    if request.method == "GET":
        matricula = request.args.get("matricula")
        # select * from alumnos where id=id
        maes1 = (
            db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        )
        nombre = maes1.nombre
        apellidos = maes1.apellidos
        email = maes1.email
        especialidad = maes1.especialidad

    return render_template(
        "maestros/detalles_a.html",
        matricula=matricula,
        nombre=nombre,
        apellidos=apellidos,
        email=email,
        especialidad=especialidad,
    )


@maestros.route("/modificar_a", methods=["GET", "POST"])
def modificar_a():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        matricula = request.args.get("matricula")
        # select * from alumnos where id=id
        maes1 = (
            db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        )
        create_form.matricula.data = maes1.matricula
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.email.data = maes1.email
        create_form.especialidad.data = maes1.especialidad
    if request.method == "POST":
        matricula = create_form.matricula.data
        maes = (
            db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        )
        maes.nombre = create_form.nombre.data
        maes.apellidos = create_form.apellidos.data
        maes.email = create_form.email.data
        maes.especialidad = create_form.especialidad.data

        db.session.add(maes)
        db.session.commit()
        return redirect(url_for("maestros.lista_maestros"))
    return render_template("maestros/modificarMest.html", form=create_form)


@maestros.route("/eliminar_a", methods=["GET", "POST"])
def eliminar_a():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        matricula = request.args.get("matricula")
        # select * from alumnos where matricula=matricula
        maes1 = (
            db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        )
        create_form.matricula.data = maes1.matricula
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.email.data = maes1.email
        create_form.especialidad.data = maes1.especialidad

    if request.method == "POST":
        matricula = create_form.matricula.data
        maes = Maestros.query.get(matricula)

        db.session.delete(maes)
        db.session.commit()
        return redirect(url_for("maestros.lista_maestros"))
    return render_template("maestros/eliminar_a.html", form=create_form)
