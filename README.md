# 🧮 Calculadora Dali PE - Modern Python GUI

Una calculadora científica moderna construida con **Python 3.11+** y **CustomTkinter**, siguiendo el patrón de diseño **MVC (Modelo-Vista-Controlador)**.

---

## 🎨 Vista Previa (ASCII)

```text
 __________________________________________
| [ BASIC MODE ]                     [ ☀ ] |
|__________________________________________|
|                                          |
|            (Historial) 12 + 5 = 17       |
|                                          |
|                    1,234.56              |
|__________________________________________|
|  [ C ]   [ DEL ]  [ % ]   [ ÷ ] (AZUL)   |
|  [ 7 ]   [ 8 ]    [ 9 ]   [ × ] (AZUL)   |
|  [ 4 ]   [ 5 ]    [ 6 ]   [ - ] (AZUL)   |
|  [ 1 ]   [ 2 ]    [ 3 ]   [ + ] (AZUL)   |
|  [ ± ]   [ 0 ]    [ . ]   [ = ] (VIOLETA)|
|  [       SCIENTIFIC MODE (SCI)       ]   |
 ------------------------------------------
```

---

## 🚀 Instalación y Uso

### 1. Requisitos
- **Python 3.11** o superior instalado.
- Entorno virtual (recomendado).

### 2. Pasos para ejecutar
```bash
# Navegar a la carpeta del proyecto
cd "PROYECTO 1"

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python main.py
```

---

## ⚙️ Características Técnicas

- **CustomTkinter**: Interfaz moderna con soporte nativo para `Dark` y `Light` mode.
- **Diseño Responsivo**: El botón `SCI` expande la ventana lateralmente para mostrar funciones científicas.
- **Soporte de Teclado**: Los dígitos, operadores y teclas especiales (`Enter`, `Escape`, `Backspace`) están vinculados.
- **Arquitectura MVC**:
  - `model.py`: Contiene toda la lógica matemática y gestión de historial.
  - `view.py`: Define los widgets, estilos y layouts.
  - `controller.py`: Maneja la interacción y binds.
- **Manejo de Errores**: Protección contra división por cero y entradas inválidas.

---

## 🛠️ Decisiones de Diseño

1. **JetBrains Mono**: Se utilizó esta fuente para el display para asegurar una lectura técnica y precisa de los dígitos.
2. **Azul Eléctrico / Violeta**: Colores de acento seleccionados para dar una sensación de herramienta de software de ingeniería moderno ("AI style").
3. **Floating Point Management**: Manejo automático de enteros/flotantes para limpiar el display (ej. `10.0` se muestra como `10`).
