import pytest

from src.pagos import SistemaPagos


def test_registrar_pago_valido():
    sistema = SistemaPagos()

    pago = sistema.registrar_pago(
        "TX-001",
        "Ana López",
        150.00
    )

    assert pago["id_transaccion"] == "TX-001"
    assert pago["estudiante"] == "Ana López"
    assert pago["valor"] == 150.00
    assert pago["estado"] == "APROBADO"
    assert sistema.contar_pagos() == 1


def test_identificador_obligatorio():
    sistema = SistemaPagos()

    with pytest.raises(
        ValueError,
        match="identificador de la transacción"
    ):
        sistema.registrar_pago("", "Ana López", 150.00)


def test_estudiante_obligatorio():
    sistema = SistemaPagos()

    with pytest.raises(
        ValueError,
        match="nombre del estudiante"
    ):
        sistema.registrar_pago("TX-002", "", 150.00)


def test_valor_cero_no_permitido():
    sistema = SistemaPagos()

    with pytest.raises(
        ValueError,
        match="mayor que cero"
    ):
        sistema.registrar_pago("TX-003", "Carlos Ruiz", 0)


def test_valor_negativo_no_permitido():
    sistema = SistemaPagos()

    with pytest.raises(
        ValueError,
        match="mayor que cero"
    ):
        sistema.registrar_pago("TX-004", "María Torres", -50.00)