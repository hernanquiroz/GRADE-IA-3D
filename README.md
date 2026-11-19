
# GRADE IA 3D v4.1

Experiencia inmersiva de investigación, educación, ciencia e inteligencia
artificial.

## Características

- Escena 3D interactiva
- Cóndor animado
- Letras GRADE
- Cerebro holográfico
- Ecosistema educativo
- Partículas y anillos holográficos
- Recorrido cinematográfico de 90 segundos
- Música ambiental generada en navegador
- Aviso institucional original
- Asistente conversacional
- Motor Groq
- Motor Gemini
- Historial de conversación por sesión
- Arquitectura preparada para ampliar funcionalidades

## Estructura

app.py
requirements.txt
README.md
.gitignore
secrets.toml.example
assets/aviso_grade_original.jpg

## Requisitos

Python 3.10 o superior.

## Instalación local

Crear entorno:

python -m venv .venv

Windows:

.venv\Scripts\activate

Linux o macOS:

source .venv/bin/activate

Instalar dependencias:

pip install -r requirements.txt

Ejecutar:

streamlit run app.py

## API de Groq

Crear una API key en:

https://console.groq.com/keys

Configurar en Streamlit Secrets:

GROQ_API_KEY = "tu_clave"

## API de Gemini

Crear una API key en:

https://aistudio.google.com/app/apikey

Configurar:

GEMINI_API_KEY = "tu_clave"

## Modelo Groq

GROQ_MODEL = "llama-3.3-70b-versatile"

## Modelo Gemini

GEMINI_MODEL = "gemini-2.5-flash"

## Seguridad

Las claves API nunca deben ser publicadas en GitHub.

Se recomienda utilizar:

- Streamlit Secrets
- Variables de entorno
- Archivo secrets local excluido de Git

## Despliegue

1. Subir archivos al repositorio GitHub.
2. Abrir Streamlit Community Cloud.
3. Crear una nueva aplicación.
4. Seleccionar el repositorio.
5. Configurar app.py como archivo principal.
6. Agregar las claves API en Settings > Secrets.
7. Desplegar.

## Aviso

El sistema es un prototipo educativo.

La inteligencia artificial puede cometer errores.
Las respuestas requieren verificación humana.
GRADE IA no sustituye el criterio académico.
