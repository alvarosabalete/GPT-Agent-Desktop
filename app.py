import openai
import subprocess
import re

# Configuración de la API de OpenAI
openai.api_key = ''

def obtener_codigo_powershell(frase):
    instrucciones = (
        "Eres un agente que solo ejecuta codigos de powershell de Windows. "
        "Si en el codigo que arrojas da error en la powershell, debes generar un codigo diferente para que se cumpla la funcionalidad que se especifica en el texto. "
        "Solo devuelve el código de PowerShell, sin ninguna explicación adicional."
    )
    prompt = f"{instrucciones}\n{frase}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instrucciones},
            {"role": "user", "content": frase}
        ]
    )
    codigo = response.choices[0].message['content'].strip()
    
    # Eliminar los marcadores de código markdown y cualquier explicación adicional
    codigo_limpio = re.sub(r'^```[\s\S]*?```$', '', codigo, flags=re.MULTILINE).strip()
    # Intentar detectar y eliminar cualquier texto explicativo adicional
    codigo_limpio = re.sub(r'^[a-zA-Z\s,\'\"()]+\:', '', codigo_limpio, flags=re.MULTILINE).strip()
    
    return codigo_limpio

def ejecutar_codigo_powershell(codigo):
    if not codigo.strip():
        return False, "El código de PowerShell está vacío o no es válido."

    try:
        # Ejecutar el comando de PowerShell
        result = subprocess.run(["powershell", "-Command", codigo], capture_output=True, text=True)
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
    except Exception as e:
        return False, str(e)

def main():
    frase = input("Escribe la frase de lo que quieres que haga: ")
    max_intentos = int(input("Número de intentos (iteraciones): "))

    for intento in range(max_intentos):
        codigo_powershell = obtener_codigo_powershell(frase)
        print(f"Intento {intento + 1}:\n{codigo_powershell}\n")
        
        exito, resultado = ejecutar_codigo_powershell(codigo_powershell)
        
        if exito:
            print(f"Éxito en el intento {intento + 1}:\n{resultado}")
            break
        else:
            print(f"Error en el intento {intento + 1}:\n{resultado}")
    else:
        print("Se alcanzó el número máximo de intentos sin éxito.")

if __name__ == "__main__":
    main()