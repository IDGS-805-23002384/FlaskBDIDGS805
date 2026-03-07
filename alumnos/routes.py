import forms
from . import alumnos
from flask import render_template, request, redirect, url_for

from models import db, Alumnos, Curso


@alumnos.route("/alumnos/listado", methods=["GET", "POST"])
def alumnos_a():
    create_form = forms.UserForm(request.form)
    alumno = Alumnos.query.all()
    return render_template("alumnos/alumnos_a.html", form=create_form, alumno=alumno)


@alumnos.route("/alumnos/Alumnos", methods=["GET", "POST"])
def alumnos_crear():
    create_form = forms.UserForm(request.form)
    if request.method == "POST":
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            telefono=create_form.telefono.data,
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("alumnos.alumnos_a"))
    return render_template("alumnos/Alumnos.html", form=create_form)


@alumnos.route("/alumnos/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
        create_form.telefono.data = alum1.telefono
    if request.method == "POST":
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        alum.telefono = create_form.telefono.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("alumnos.alumnos_a"))
    return render_template("alumnos/modificar.html", form=create_form)


@alumnos.route("/alumnos/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
        create_form.telefono.data = alum1.telefono
    if request.method == "POST":
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for("alumnos.alumnos_a"))
    return render_template("alumnos/eliminar.html", form=create_form)


@alumnos.route("/alumnos/detalles", methods=["GET", "POST"])
def detalles():
    id = request.args.get("id")
    alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    return render_template(
        "alumnos/detalles.html",
        id=id,
        nombre=alum1.nombre,
        apellidos=alum1.apellidos,
        email=alum1.email,
        telefono=alum1.telefono,
    )


@alumnos.route("/alumnos/<int:id>/cursos", methods=["GET"])
def ver_cursos_alumno(id):
    alumno = Alumnos.query.get(id)
    if not alumno:
        return redirect(url_for("alumnos.alumnos_a"))

    return render_template(
        "alumnos/cursos_alumno.html", alumno=alumno, cursos=alumno.cursos
    )


@alumnos.route("/alumnos/<int:id>/cursos/inscribir", methods=["GET", "POST"])
def inscribir_curso_alumno(id):
    alumno = Alumnos.query.get(id)
    if not alumno:
        return redirect(url_for("alumnos.alumnos_a"))

    cursos_disponibles = Curso.query.filter(
        ~Curso.id.in_([c.id for c in alumno.cursos])
    ).all()

    if request.method == "POST":
        curso_id = request.form.get("curso_id")
        if curso_id:
            curso = Curso.query.get(curso_id)
            if curso and curso not in alumno.cursos:
                alumno.cursos.append(curso)
                db.session.commit()
                return redirect(url_for("alumnos.ver_cursos_alumno", id=id))

    return render_template(
        "alumnos/inscribir_curso.html", alumno=alumno, cursos=cursos_disponibles
    )


@alumnos.route(
    "/alumnos/<int:alumno_id>/cursos/<int:curso_id>/desinscribir", methods=["POST"]
)
def desinscribir_curso_alumno(alumno_id, curso_id):
    alumno = Alumnos.query.get(alumno_id)
    curso = Curso.query.get(curso_id)

    if alumno and curso and curso in alumno.cursos:
        alumno.cursos.remove(curso)
        db.session.commit()

    return redirect(url_for("alumnos.ver_cursos_alumno", id=alumno_id))
