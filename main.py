from database import init_db
from page import cargar_interfaz
from nicegui import ui


init_db()
cargar_interfaz()
ui.run(title='Gestionar tareas', port=8081)