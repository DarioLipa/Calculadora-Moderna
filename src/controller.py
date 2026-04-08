import src.config as config
from src.model import CalculatorModel
from typing import Optional

class CalculatorController:
    """
    Controlador que conecta el modelo con la vista.
    Gestiona los eventos del teclado y los clics en botones.
    """

    def __init__(self, model: CalculatorModel, view):
        self.model = model
        self.view = view
        
        # Vincular teclas del teclado
        self._bind_keys()

    def handle_click(self, btn_text: str):
        """Procesa la acción de un botón clickeado."""
        
        if btn_text == "C":
            self.model.clear()
        elif btn_text == "DEL":
            self.model.delete()
        elif btn_text == "=":
            self.model.calculate()
        elif btn_text == "SCI":
            self.view.toggle_scientific()
            return # No actualizar display todavía
        elif btn_text in ["√", "x²", "1/x", "log", "ln", "sin", "cos", "tan", "±", "%"]:
            self.model.scientific_op(btn_text)
        elif btn_text == "π":
             self.model.add_to_expression("3.14159")
        elif btn_text == "xⁿ":
             self.model.add_to_expression("**")
        else:
            self.model.add_to_expression(btn_text)

        # Actualizar la vista
        self.view.update_display(self.model.current_value, self.model.get_history())

    def _bind_keys(self):
        """Enlaza las teclas físicas a las funciones del controlador."""
        for key, value in config.KEY_BINDINGS.items():
            self.view.bind(f"<{key}>", lambda event, v=value: self.handle_click(v))
        
        # Binds para números del teclado
        for i in range(10):
            self.view.bind(f"{i}", lambda event, digit=str(i): self.handle_click(digit))
        
        # Enter (Return)
        self.view.bind("<Return>", lambda event: self.handle_click("="))
        self.view.bind("<BackSpace>", lambda event: self.handle_click("DEL"))
        self.view.bind("<Escape>", lambda event: self.handle_click("C"))
