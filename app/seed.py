from datetime import date, time
import click
from app import db


def registrar_seed(app):
    @app.cli.command("seed")
    def seed():
        """Carga datos de prueba en las tablas."""
        from app.medicos.models import Medico
        from app.pacientes.models import Paciente
        from app.citas.models import Cita

        if Medico.query.first():
            click.echo("La base ya tiene datos. No se cargó nada.")
            return

        m1 = Medico(nombre="Dr. Carlos Rojas", especialidad="Cardiología")
        m2 = Medico(nombre="Dra. Lucía Mendoza", especialidad="Pediatría")
        m3 = Medico(nombre="Dr. Jorge Vargas", especialidad="Medicina General")

        p1 = Paciente(nombre="Ana Quispe", telefono="71234567")
        p2 = Paciente(nombre="Luis Mamani", telefono="72345678")
        p3 = Paciente(nombre="María Flores", telefono="73456789")

        db.session.add_all([
            m1, m2, m3, p1, p2, p3,
            Cita(fecha=date(2026, 11, 10), hora=time(8, 30), medico=m1, paciente=p1),
            Cita(fecha=date(2026, 11, 10), hora=time(10, 0), medico=m2, paciente=p2),
            Cita(fecha=date(2026, 11, 11), hora=time(9, 15), medico=m3, paciente=p3),
            Cita(fecha=date(2026, 11, 12), hora=time(15, 0), medico=m1, paciente=p2),
        ])
        db.session.commit()
        click.echo("Datos de prueba cargados: 3 médicos, 3 pacientes y 4 citas.")