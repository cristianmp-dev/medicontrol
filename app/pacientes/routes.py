from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.pacientes.models import Paciente

bp_pacientes = Blueprint("bp_pacientes", __name__, template_folder="templates")


@bp_pacientes.route("/")
def lista():
    pacientes = Paciente.query.order_by(Paciente.nombre).all()
    return render_template("pacientes_lista.html", pacientes=pacientes)


@bp_pacientes.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        paciente = Paciente(nombre=request.form["nombre"], telefono=request.form["telefono"])
        db.session.add(paciente)
        db.session.commit()
        flash("Paciente registrado.", "success")
        return redirect(url_for("bp_pacientes.lista"))
    return render_template("pacientes_form.html", paciente=None)


@bp_pacientes.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    paciente = db.get_or_404(Paciente, id)
    if request.method == "POST":
        paciente.nombre = request.form["nombre"]
        paciente.telefono = request.form["telefono"]
        db.session.commit()
        flash("Paciente modificado.", "success")
        return redirect(url_for("bp_pacientes.lista"))
    return render_template("pacientes_form.html", paciente=paciente)


@bp_pacientes.route("/<int:id>/eliminar", methods=["POST"])
def eliminar(id):
    paciente = db.get_or_404(Paciente, id)
    if paciente.citas:
        flash("No se puede eliminar: el paciente tiene citas registradas.", "warning")
    else:
        db.session.delete(paciente)
        db.session.commit()
        flash("Paciente eliminado.", "success")
    return redirect(url_for("bp_pacientes.lista"))