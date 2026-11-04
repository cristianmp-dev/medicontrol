import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "clave-secreta-medicontrol"
    # Base de datos SQLite como archivo "medicontrol.db"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "medicontrol.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False