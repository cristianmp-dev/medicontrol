from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """Application Factory: crea y configura la aplicación."""
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Modelos (para que Flask-Migrate los detecte)
    from app.medicos.models import Medico
    from app.pacientes.models import Paciente
    from app.citas.models import Cita

    # Blueprints con sus prefijos
    from app.medicos.routes import bp_medicos
    from app.pacientes.routes import bp_pacientes
    from app.citas.routes import bp_citas

    app.register_blueprint(bp_medicos, url_prefix="/medicos")
    app.register_blueprint(bp_pacientes, url_prefix="/pacientes")
    app.register_blueprint(bp_citas, url_prefix="/citas")

    @app.route("/")
    def inicio():
        return render_template(
            "inicio.html",
            total_medicos=Medico.query.count(),
            total_pacientes=Paciente.query.count(),
            citas=Cita.query.order_by(Cita.fecha, Cita.hora).all(),
        )

    from app.seed import registrar_seed
    registrar_seed(app)

    return app