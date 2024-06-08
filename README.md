# Generador y Ejecutor de Código PowerShell

Este script en Python utiliza la API de OpenAI para generar código de PowerShell que cumpla con un requisito especificado en un texto de entrada. Luego, ejecuta este código generado en un entorno de PowerShell de Windows y devuelve el resultado.

## Instalación

1. Clona o descarga el repositorio en tu máquina local.
2. Instala las dependencias ejecutando `pip install -r requirements.txt`.
3. Configura tu clave de API de OpenAI en el script `openai.api_key = `.

## Uso

1. Ejecuta el script `codigo_powershell.py`.
2. Ingresa la frase que describa el comportamiento deseado del código de PowerShell.
3. Define el número máximo de intentos (iteraciones) que el script realizará para generar y ejecutar el código.
4. El script generará y ejecutará el código de PowerShell. Si tiene éxito, mostrará el resultado. Si falla, mostrará un mensaje de error.

## Notas

- Asegúrate de tener una conexión a Internet activa para que el script pueda acceder a la API de OpenAI.
- Ten en cuenta que la generación de código de PowerShell puede no ser siempre perfecta. Es posible que necesites ajustar manualmente el código generado según tus necesidades específicas.
