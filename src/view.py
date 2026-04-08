import customtkinter as ctk
from PIL import Image
from typing import Callable, List, Optional
import src.config as config

class CalculatorView(ctk.CTk):
    """
    Clase que define la interfaz gráfica de la calculadora científica.
    Sigue el patrón MVC (View).
    """

    def __init__(self, controller_callback: Callable):
        super().__init__()
        
        self.controller_callback = controller_callback
        self.title("Calculadora Dali PE")
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.configure(fg_color=(config.COLOR_BG_LIGHT, config.COLOR_BG_DARK))

        # Configuración de CustomTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Variables de estado
        self.scientific_mode = False

        # --- Crear Componentes ---
        self._setup_ui()

    def _setup_ui(self):
        """Inicializa los elementos de la interfaz."""
        
        # Grid Principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # 1. BARRA SUPERIOR (MODO Y TEMA)
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(15, 5))
        
        self.mode_label = ctk.CTkLabel(
            self.header_frame, 
            text="MODO BASICO", 
            font=(config.FONT_BUTTONS[0], 12),
            text_color=config.COLOR_ACCENT
        )
        self.mode_label.pack(side="left")

        self.theme_toggle = ctk.CTkButton(
            self.header_frame, 
            text=" ☾ ", 
            width=30, 
            height=30,
            corner_radius=15,
            fg_color=config.COLOR_BG_SECONDARY_DARK,
            hover_color=config.COLOR_ACCENT,
            command=self.toggle_theme
        )
        self.theme_toggle.pack(side="right")

        # 2. DISPLAY (HISTORIAL + VALOR ACTUAL)
        self.display_frame = ctk.CTkFrame(self, fg_color=(config.COLOR_BG_SECONDARY_LIGHT, config.COLOR_BG_SECONDARY_DARK), corner_radius=20)
        self.display_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)
        
        self.history_label = ctk.CTkLabel(
            self.display_frame, 
            text="", 
            font=config.FONT_HISTORY,
            text_color=config.COLOR_TEXT_SECONDARY,
            anchor="e"
        )
        self.history_label.pack(fill="x", padx=20, pady=(15, 0))

        self.display_label = ctk.CTkLabel(
            self.display_frame, 
            text="0", 
            font=config.FONT_DIGITS,
            text_color=config.COLOR_TEXT_PRIMARY,
            anchor="e"
        )
        self.display_label.pack(fill="x", padx=20, pady=(0, 15))

        # 3. BOTONERA (GRID)
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=(10, 20))
        
        # Grid para botones (4 columnas base)
        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.buttons_frame.grid_rowconfigure(i, weight=1)

        self._create_buttons()

    def _create_buttons(self):
        """Crea la cuadrícula de botones básica."""
        
        buttons_data = [
            ('C', 0, 0, '#FF4B4B'), ('DEL', 0, 1, '#4A5568'), ('%', 0, 2, '#4A5568'), ('÷', 0, 3, config.COLOR_ACCENT),
            ('7', 1, 0, None), ('8', 1, 1, None), ('9', 1, 2, None), ('×', 1, 3, config.COLOR_ACCENT),
            ('4', 2, 0, None), ('5', 2, 1, None), ('6', 2, 2, None), ('-', 2, 3, config.COLOR_ACCENT),
            ('1', 3, 0, None), ('2', 3, 1, None), ('3', 3, 2, None), ('+', 3, 3, config.COLOR_ACCENT),
            ('±', 4, 0, None), ('0', 4, 1, None), ('.', 4, 2, None), ('=', 4, 3, config.COLOR_ACCENT_ALT),
            ('SCI', 5, 0, config.COLOR_ACCENT, 4) # El botón SCI ocupa toda la fila
        ]

        self.btns = {}
        for btn_text, r, c, color, *extra in buttons_data:
            colspan = extra[0] if extra else 1
            
            fg = color if color else config.COLOR_BG_SECONDARY_DARK
            hover = config.COLOR_ACCENT_ALT if not color else color
            
            btn = ctk.CTkButton(
                self.buttons_frame,
                text=btn_text,
                font=config.FONT_BUTTONS,
                width=0,
                height=60,
                corner_radius=config.CORNER_RADIUS,
                fg_color=fg,
                hover_color=hover,
                command=lambda x=btn_text: self.controller_callback(x)
            )
            btn.grid(row=r, column=c, columnspan=colspan, sticky="nsew", padx=config.BUTTON_PADDING, pady=config.BUTTON_PADDING)
            self.btns[btn_text] = btn

    def toggle_scientific(self):
        """Expande o contrae el panel científico."""
        self.scientific_mode = not self.scientific_mode
        
        if self.scientific_mode:
            self.geometry(f"{config.WINDOW_WIDTH + 200}x{config.WINDOW_HEIGHT}")
            self.mode_label.configure(text="MODO CIENTIFICO", text_color=config.COLOR_ACCENT_ALT)
            self._show_sci_panel()
        else:
            self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
            self.mode_label.configure(text="MODO BASICO", text_color=config.COLOR_ACCENT)
            self._hide_sci_panel()

    def _show_sci_panel(self):
        """Crea y muestra el panel lateral científico."""
        self.sci_frame = ctk.CTkFrame(self, fg_color="transparent", width=180)
        self.sci_frame.grid(row=0, column=1, rowspan=3, sticky="nsew", padx=(0, 20), pady=20)
        
        sci_ops = [
            'sin', 'cos', 'tan',
            'log', 'ln', '√',
            'x²', 'xⁿ', 'π',
            '1/x', '(', ')'
        ]
        
        for i, op in enumerate(sci_ops):
            btn = ctk.CTkButton(
                self.sci_frame,
                text=op,
                font=config.FONT_SCIENTIFIC,
                width=80,
                height=50,
                corner_radius=config.CORNER_RADIUS,
                fg_color=config.COLOR_BG_SECONDARY_DARK,
                hover_color=config.COLOR_ACCENT_ALT,
                command=lambda x=op: self.controller_callback(x)
            )
            btn.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="nsew")

    def _hide_sci_panel(self):
        """Destruye el panel científico."""
        if hasattr(self, 'sci_frame'):
            self.sci_frame.destroy()

    def update_display(self, current: str, history: List[str]):
        """Actualiza las etiquetas del display."""
        self.display_label.configure(text=current)
        if history:
            self.history_label.configure(text=history[-1])
        else:
            self.history_label.configure(text="")

    def toggle_theme(self):
        """Cambia entre modo claro y oscuro."""
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)
        
        icon = " ☀ " if new_mode == "Dark" else " ☾ "
        self.theme_toggle.configure(text=icon)
