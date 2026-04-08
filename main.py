import sys
import os
from src.model import CalculatorModel
from src.view import CalculatorView
from src.controller import CalculatorController

def main():
    """
    Punto de entrada de la aplicación.
    Inicializa los componentes del patrón MVC y arranca el loop principal.
    """
    
    # Asegurarnos de que estamos en el directorio raíz
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    # 1. Crear Modelo
    model = CalculatorModel()

    # 2. Crear Controlador (pasamos referencia al modelo)
    # Nota: El controlador necesita la vista para bindear teclas, 
    # pero la vista necesita una callback del controlador para los botones.
    # Usamos una función puente para evitar circularidad en la inicialización simple.
    
    controller = None

    def bridge_callback(btn_text: str):
        if controller:
            controller.handle_click(btn_text)

    # 3. Crear Vista (le pasamos la función callback)
    view = CalculatorView(bridge_callback)

    # 4. Inicializar Controlador (le pasamos modelo y vista)
    controller = CalculatorController(model, view)

    # 5. Configurar vista con controlador
    view.controller_callback = controller.handle_click

    # Iniciar aplicación
    view.mainloop()

if __name__ == "__main__":
    main()
