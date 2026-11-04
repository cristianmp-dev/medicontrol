from datetime import date, time
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.citas.models import Cita
from app.medicos.models import Medico
from app.pacientes.models import Paciente

bp_citas = Blueprint("bp_citas", __name__, template_folder="templates")


def datos_formulario():
    """Listas para los selectores del formulario."""
    return {
        "medicos": Medico.query.order_by(Medico.nombre).all(),
        "pacientes": Paciente.query.order_by(Paciente.nombre).all(),
    }


def guardar_datos(cita):
    cita.fecha = date.fromisoformat(request.form["fecha"])
    cita.hora = time.fromisoformat(request.form["hora"])
    cita.medico_id = int(request.form["medico_id"])
    cita.paciente_id = int(request.form["paciente_id"])


@bp_citas.route("/")
def lista():
    citas = Cita.query.order_by(Cita.fecha, Cita.hora).all()
    return render_template("citas_lista.html", citas=citas)


@bp_citas.route("/nueva", methods=["GET", "POST"])
def nueva():
    if request.method == "POST":
        cita = Cita()
        guardar_datos(cita)
        db.session.add(cita)
        db.session.commit()
        flash("Cita registrada.", "success")
        return redirect(url_for("bp_citas.lista"))
    return render_template("citas_form.html", cita=None, **datos_formulario())


@bp_citas.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    cita = db.get_or_404(Cita, id)
    if request.method == "POST":
        guardar_datos(cita)
        db.session.commit()
        flash("Cita modificada.", "success")
        return redirect(url_for("bp_citas.lista"))
    return render_template("citas_form.html", cita=cita, **datos_formulario())


@bp_citas.route("/<int:id>/eliminar", methods=["POST"])
def eliminar(id):
    cita = db.get_or_404(Cita, id)
    db.session.delete(cita)
    db.session.commit()
    flash("Cita eliminada.", "success")
    return redirect(url_for("bp_citas.lista"))