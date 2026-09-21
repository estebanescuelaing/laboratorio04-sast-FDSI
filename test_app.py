from app import ejecutar_comando


def test_opcion_permitida():
    resultado = ejecutar_comando("version")

    assert resultado


def test_opcion_no_permitida():
    resultado = ejecutar_comando("comando_no_permitido")

    assert resultado == "Comando no permitido"
