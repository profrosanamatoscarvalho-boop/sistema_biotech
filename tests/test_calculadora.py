import pytest
from calculadora import CalculadoraBiotech

def test_calcular_diluicao_sucesso():
    # C1=10, V1=2, C2=2 -> V2 deve ser 10
    assert CalculadoraBiotech.calcular_diluicao(10.0, 2.0, 2.0) == 10.0

def test_calcular_massa_molar_sucesso():
    # n=2, MM=180 -> m deve ser 360
    assert CalculadoraBiotech.calcular_massa_molar(2.0, 180.0) == 360.0
