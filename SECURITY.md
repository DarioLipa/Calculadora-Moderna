# Política de Seguridad

Este documento describe cómo se deben reportar las vulnerabilidades encontradas en este proyecto.

## Reportar una Vulnerabilidad

Si encuentras una vulnerabilidad de seguridad en este proyecto, por favor NO abras un "Issue" público. En su lugar, contacta directamente con el desarrollador o envía un reporte detallado si existe un canal específico.

## Medidas de Seguridad Implementadas

1. **Evaluación Segura:** Todas las expresiones matemáticas son validadas mediante expresiones regulares antes de ser procesadas por el motor de cálculo.
2. **Entorno Restringido:** El cálculo se realiza en un entorno sin acceso a las funciones globales de Python (`__builtins__`).
3. **Gestión de Errores:** Se han implementado capturas de excepciones para evitar que fallos en el cálculo comprometan la estabilidad de la aplicación.
