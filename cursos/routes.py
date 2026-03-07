from . import cursos
from flask import render_template, request, redirect, url_for
from models import db, Curso, Maestros, Alumnos
import forms


@cursos.route("/cursos/listado", methods=["GET"])
def lista_cursos():
    cursos = Curso.query.all()
    return render_template("cursos/listado.html", cursos=cursos)


@cursos.route("/cursos/crear", methods=["GET", "POST"])
def crear_curso():
    create_form = forms.CursoForm(request.form)

    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [
        (m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros
    ]

    if request.method == "POST" and create_form.validate():
        curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data,
        )
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for("cursos.lista_cursos"))

    return render_template("cursos/crear.html", form=create_form)


@cursos.route("/cursos/modificar", methods=["GET", "POST"])
def modificar_curso():
    create_form = forms.CursoForm(request.form)

    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [
        (m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros
    ]

    if request.method == "GET":
        id = request.args.get("id")
        curso = Curso.query.get(id)
        if curso:
            create_form.id.data = curso.id
            create_form.nombre.data = curso.nombre
            create_form.descripcion.data = curso.descripcion
            create_form.maestro_id.data = curso.maestro_id

    if request.method == "POST":
        id = create_form.id.data
        curso = Curso.query.get(id)
        if curso:
            curso.nombre = create_form.nombre.data
            curso.descripcion = create_form.descripcion.data
            curso.maestro_id = create_form.maestro_id.data
            db.session.commit()
            return redirect(url_for("cursos.lista_cursos"))

    return render_template("cursos/modificar.html", form=create_form)


@cursos.route("/cursos/eliminar", methods=["GET", "POST"])
def eliminar_curso():
    create_form = forms.CursoForm(request.form)

    if request.method == "GET":
        id = request.args.get("id")
        curso = Curso.query.get(id)
        if curso:
            create_form.id.data = curso.id
            create_form.nombre.data = curso.nombre
            create_form.descripcion.data = curso.descripcion

    if request.method == "POST":
        id = create_form.id.data
        curso = Curso.query.get(id)
        if curso:
            db.session.delete(curso)
            db.session.commit()
            return redirect(url_for("cursos.lista_cursos"))

    return render_template("cursos/eliminar.html", form=create_form)


@cursos.route("/cursos/<int:id>/alumnos", methods=["GET"])
def ver_alumnos_curso(id):
    curso = Curso.query.get(id)
    if not curso:
        return redirect(url_for("cursos.lista_cursos"))

    return render_template(
        "cursos/alumnos_curso.html", curso=curso, alumnos=curso.alumnos
    )


@cursos.route("/cursos/<int:id>/agregar-alumno", methods=["GET", "POST"])
def agregar_alumno_curso(id):
    curso = Curso.query.get(id)
    if not curso:
        return redirect(url_for("cursos.lista_cursos"))

    alumnos_disponibles = Alumnos.query.filter(
        ~Alumnos.id.in_([a.id for a in curso.alumnos])
    ).all()

    if request.method == "POST":
        alumno_id = request.form.get("alumno_id")
        if alumno_id:
            alumno = Alumnos.query.get(alumno_id)
            if alumno and alumno not in curso.alumnos:
                curso.alumnos.append(alumno)
                db.session.commit()
                return redirect(url_for("cursos.ver_alumnos_curso", id=id))

    return render_template(
        "cursos/agregar_alumno.html", curso=curso, alumnos=alumnos_disponibles
    )


@cursos.route(
    "/cursos/<int:curso_id>/alumnos/<int:alumno_id>/remover", methods=["POST"]
)
def remover_alumno_curso(curso_id, alumno_id):
    curso = Curso.query.get(curso_id)
    alumno = Alumnos.query.get(alumno_id)

    if curso and alumno and alumno in curso.alumnos:
        curso.alumnos.remove(alumno)
        db.session.commit()

    return redirect(url_for("cursos.ver_alumnos_curso", id=curso_id))
