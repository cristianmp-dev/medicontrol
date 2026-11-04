from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.medicos.models import Medico

bp_medicos = Blueprint("bp_medicos", __name__, template_folder="templates")


@bp_medicos.route("/")
def lista():
    medicos = Medico.query.order_by(Medico.nombre).all()
    return render_template("medicos_lista.html", medicos=medicos)


@bp_medicos.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        medico = Medico(nombre=request.form["nombre"], especialidad=request.form["especialidad"])
        db.session.add(medico)
        db.session.commit()
        flash("Médico registrado.", "success")
        return redirect(url_for("bp_medicos.lista"))
    return render_template("medicos_form.html", medico=None)


@bp_medicos.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    medico = db.get_or_404(Medico, id)
    if request.method == "POST":
        medico.nombre = request.form["nombre"]
        medico.especialidad = request.form["especialidad"]
        db.session.commit()
        flash("Médico modificado.", "success")
        return redirect(url_for("bp_medicos.lista"))
    return render_template("medicos_form.html", medico=medico)


@bp_medicos.route("/<int:id>/eliminar", methods=["POST"])
def eliminar(id):
    medico = db.get_or_404(Medico, id)
    if medico.citas:
        flash("No se puede eliminar: el médico tiene citas registradas.", "warning")
    else:
        db.session.delete(medico)
        db.session.commit()
        flash("Médico eliminado.", "success")
    return redirect(url_for("bp_medicos.lista"))