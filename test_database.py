import sqlite3

from database import buscar_usuario


def test_buscar_usuario(tmp_path, monkeypatch):
    database_path = tmp_path / "laboratorio.db"

    conexion = sqlite3.connect(database_path)
    cursor = conexion.cursor()

    cursor.execute(
        "CREATE TABLE usuarios (id INTEGER, nombre TEXT)"
    )

    cursor.execute(
        "INSERT INTO usuarios VALUES (?, ?)",
        (1, "Esteban")
    )

    conexion.commit()
    conexion.close()

    monkeypatch.chdir(tmp_path)

    resultado = buscar_usuario("Esteban")

    assert len(resultado) == 1
    assert resultado[0][1] == "Esteban"


def test_buscar_usuario_sin_resultados(tmp_path, monkeypatch):
    database_path = tmp_path / "laboratorio.db"

    conexion = sqlite3.connect(database_path)
    cursor = conexion.cursor()

    cursor.execute(
        "CREATE TABLE usuarios (id INTEGER, nombre TEXT)"
    )

    conexion.commit()
    conexion.close()

    monkeypatch.chdir(tmp_path)

    resultado = buscar_usuario("Usuario inexistente")

    assert resultado == []
