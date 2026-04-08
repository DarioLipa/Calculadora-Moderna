import math
from typing import List, Tuple, Optional

class CalculatorModel:
    """
    Clase que maneja toda la lógica de cálculo y el historial de la calculadora.
    Sigue el patrón MVC (Model).
    """

    def __init__(self):
        self.current_value: str = "0"
        self.history: List[str] = []
        self.expression: str = ""
        self.max_history: int = 10

    def add_to_expression(self, char: str) -> None:
        """Añade un carácter a la expresión actual."""
        if self.current_value == "0" and char not in ".":
             self.current_value = char
        else:
             self.current_value += char

    def clear(self) -> None:
        """Limpia el valor actual y la expresión."""
        self.current_value = "0"
        self.expression = ""

    def delete(self) -> None:
        """Borra el último carácter introducido."""
        if len(self.current_value) > 1:
            self.current_value = self.current_value[:-1]
        else:
            self.current_value = "0"

    def calculate(self) -> None:
        """Evalúa la expresión actual y guarda en el historial."""
        try:
            # Reemplazamos símbolos para evaluación en Python
            expr = self.current_value.replace('×', '*').replace('÷', '/')
            result = eval(expr)
            
            # Formatear el resultado
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            # Guardar en el historial
            self.history.append(f"{self.current_value} = {result}")
            if len(self.history) > self.max_history:
                self.history.pop(0)

            self.current_value = str(result)
        except ZeroDivisionError:
            self.current_value = "Error: Div / 0"
        except Exception:
            self.current_value = "Error"

    def scientific_op(self, op: str) -> None:
        """Ejecuta operaciones científicas directamente sobre el valor actual."""
        try:
            val = float(self.current_value)
            result = 0.0

            if op == "√":
                result = math.sqrt(val)
            elif op == "x²":
                result = val ** 2
            elif op == "1/x":
                result = 1 / val
            elif op == "log":
                result = math.log10(val)
            elif op == "ln":
                result = math.log(val)
            elif op == "sin":
                result = math.sin(math.radians(val))
            elif op == "cos":
                result = math.cos(math.radians(val))
            elif op == "tan":
                result = math.tan(math.radians(val))
            elif op == "±":
                result = -val
            elif op == "%":
                 result = val / 100

            # Formatear resultado
            if result.is_integer():
                result = int(result)
            
            self.history.append(f"{op}({val}) = {result}")
            if len(self.history) > self.max_history:
                self.history.pop(0)
                
            self.current_value = str(result)
        except ValueError:
            self.current_value = "Error: Input"
        except ZeroDivisionError:
            self.current_value = "Error: Div / 0"
        except Exception:
            self.current_value = "Error"

    def get_history(self) -> List[str]:
        """Devuelve el historial actual."""
        return self.history
