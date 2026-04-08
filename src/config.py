"""
Configuración global para la calculadora científica.
Define colores, fuentes, y parámetros de diseño.
"""

# Colores Dark Theme
COLOR_BG_DARK = "#0D0D0D"
COLOR_BG_SECONDARY_DARK = "#111827"
COLOR_ACCENT = "#00AAFF"  # Azul Eléctrico
COLOR_ACCENT_ALT = "#7C3AED"  # Violeta
COLOR_TEXT_PRIMARY = "#FFFFFF"
COLOR_TEXT_SECONDARY = "#94A3B8"

# Colores Light Theme (Opcional, CustomTkinter maneja el cambio pero podemos definir acentos)
COLOR_BG_LIGHT = "#F8FAFC"
COLOR_BG_SECONDARY_LIGHT = "#F1F5F9"
COLOR_TEXT_PRIMARY_LIGHT = "#0F172A"

# Tipografías
FONT_DIGITS = ("JetBrains Mono", 36, "bold")
FONT_HISTORY = ("JetBrains Mono", 14)
FONT_BUTTONS = ("Inter", 18, "bold")
FONT_SCIENTIFIC = ("Inter", 14, "normal")

# Dimensiones y Padding
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 650
CORNER_RADIUS = 12
BUTTON_PADDING = 5
DISPLAY_PADDING = 15

# Teclas de Bind (Teclado)
KEY_BINDINGS = {
    'Return': '=',
    'Escape': 'C',
    'BackSpace': 'DEL',
    'plus': '+',
    'minus': '-',
    'asterisk': '*',
    'slash': '/',
    'period': '.',
    'percent': '%',
}
