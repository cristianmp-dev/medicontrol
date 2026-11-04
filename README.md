# MediControl (Flask + Application Factory)

Sistema monolítico modular para la gestión de médicos, pacientes y citas médicas con Flask, Flask-SQLAlchemy, Flask-Migrate (SQLite) y Bootstrap 5.

**Requisito:** Python 3.11 o superior.

## Cómo ejecutar

### Paso 1: descargar el proyecto

```bash
git clone https://github.com/TU-USUARIO/medicontrol.git
cd medicontrol
```

### Paso 2: crear y activar el entorno virtual

**Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\activate
```

> Si PowerShell dice que la ejecución de scripts está deshabilitada, ejecutar
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a activar.

### Paso 3: instalar, crear la base de datos y ejecutar (igual en Linux y Windows)

```bash
pip install -r requirements.txt
flask db upgrade
flask seed
flask run
```

### Paso 4: abrir la aplicación

Abrir http://127.0.0.1:5000