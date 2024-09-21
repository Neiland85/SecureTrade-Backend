[flake8]
# Ignorar reglas de estilo específicas (como líneas largas y espacio antes de :)
ignore = E501,E203,W391
# Excluir el directorio venv/ de la revisión de flake8
exclude = venv/
# Permitir líneas más largas de lo normal, hasta 120 caracteres
max-line-length = 120