import sqlite3


def buscar_usuario(nombre):
    conexion = sqlite3.connect("laboratorio.db")
    cursor = conexion.cursor()

    # Vulnerabilidad intencional: SQL Injection
    consulta = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "'"

    cursor.execute(consulta)
    resultado = cursor.fetchall()

    conexion.close()
    return resultado


if __name__ == "__main__":
    nombre = input("Nombre del usuario: ")
    print(buscar_usuario(nombre))
