import subprocess


COMANDOS_PERMITIDOS = {
    "listar": ["python", "--version"],
    "version": ["python", "--version"]
}


def ejecutar_comando(opcion):
    if opcion not in COMANDOS_PERMITIDOS:
        return "Comando no permitido"

    resultado = subprocess.run(
        COMANDOS_PERMITIDOS[opcion],
        shell=False,
        capture_output=True,
        text=True
    )

    return resultado.stdout


if __name__ == "__main__":
    opcion = input("Opción de laboratorio: ")
    print(ejecutar_comando(opcion))
