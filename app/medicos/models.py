from app import db


class Medico(db.Model):
    __tablename__ = "medicos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)

    # Un médico puede tener muchas citas
    citas = db.relationship("Cita", back_populates="medico")