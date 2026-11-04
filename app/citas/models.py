from app import db


class Cita(db.Model):
    __tablename__ = "citas"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey("medicos.id"), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey("pacientes.id"), nullable=False)

    # Cada cita pertenece a un médico y a un paciente
    medico = db.relationship("Medico", back_populates="citas")
    paciente = db.relationship("Paciente", back_populates="citas")