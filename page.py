from nicegui import ui
from database import agregar_tarea, obtener_tareas

# Cargar Interfaz de Usuario
def cargar_interfaz():
    ui.label('Gestor de Tareas').classes('text-2xl font-bold text-blue-700 mb-4')
    
    with ui.card().classes('w-full max-w-md p-4 mb-4 shadow-lg'):
        input_tarea = ui.input(placeholder='Escribe una nueva tarea...').classes('w-full')
        
        def guardar():
            if input_tarea.value.strip():
                agregar_tarea(input_tarea.value.strip())
                ui.notify(f'Tarea guardada: {input_tarea.value}', color='positive')
                input_tarea.value = ''
                render_lista.refresh()
                
        ui.button('Guardar Tarea', on_click=guardar).classes('w-full mt-2 bg-teal-600 text-white')
    
    @ui.refreshable
    def render_lista():
        tareas = obtener_tareas()
        ui.label(f'Total de Tareas: {len(tareas)}').classes('font-semibold text-gray-700 mb-2')
        with ui.list().classes('w-full max-w-md bg-white rounded-lg border'):
            for t in tareas:
                estado = "✅" if t.completada else "⏳"
                ui.item(f'{estado} {t.titulo}')
                
    render_lista()


# Si este es tu archivo principal (main.py), recuerda agregar esta línea al final:
if __name__ in {"__main__", "__mp_main__"}:
    cargar_interfaz()
    ui.run()