import subprocess


def ejecutar_comando(comando):
    # Vulnerabilidad intencional: Command Injection
    resultado = subprocess.run(
        comando,
        shell=True,
        capture_output=True,
        text=True
    )

    return resultado.stdout


if __name__ == "__main__":
    comando = input("Comando de laboratorio: ")
    print(ejecutar_comando(comando))
