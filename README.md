# PowerShell Code Generator and Executor

This Python script utilizes the OpenAI API to generate PowerShell code that fulfills a specified requirement provided as input text. Subsequently, it executes this generated code within a Windows PowerShell environment and returns the result.

## Installation

1. Clone or download the repository to your local machine.
2. Install dependencies by running `pip install -r requirements.txt`.
3. Configure your OpenAI API key in the script `openai.api_key = ''`.

## Usage

1. Execute the script `app.py`.
2. Input the phrase describing the desired behavior of the PowerShell code.
3. Define the maximum number of attempts (iterations) the script will make to generate and execute the code.
4. The script will generate and execute the PowerShell code. If successful, it will display the result. If it fails, it will show an error message.

---

# Generador y Ejecutor de Código PowerShell

Este script en Python utiliza la API de OpenAI para generar código de PowerShell que cumpla con un requisito especificado en un texto de entrada. Luego, ejecuta este código generado en un entorno de PowerShell de Windows y devuelve el resultado.

## Instalación

1. Clona o descarga el repositorio en tu máquina local.
2. Instala las dependencias ejecutando `pip install -r requirements.txt`.
3. Configura tu clave de API de OpenAI en el script `openai.api_key = `.

## Uso

1. Ejecuta el script `app.py`.
2. Ingresa la frase que describa el comportamiento deseado del código de PowerShell.
3. Define el número máximo de intentos (iteraciones) que el script realizará para generar y ejecutar el código.
4. El script generará y ejecutará el código de PowerShell. Si tiene éxito, mostrará el resultado. Si falla, mostrará un mensaje de error.
