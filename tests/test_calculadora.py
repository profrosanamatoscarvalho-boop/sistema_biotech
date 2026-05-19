import pytest
from app.calculadora import CalculadoraMolaridade

def test_preparo_solucao_valida():
    # Exemplo: Preparar 1 Litro de solução 1M de NaCl (Massa Molar aprox. 58.44 g/mol)
    # Resultado esperado: 1 * 1 * 58.44 = 58.44 gramas
    calc = CalculadoraMolaridade(58.44, 1.0, 1.0)
    assert calc.calcular_massa_soluto() == 58.44

def test_valores_negativos_geram_erro():
    # Concentração ou volume negativo deve disparar erro do sistema
    with pytest.raises(ValueError):
        calc = CalculadoraMolaridade(58.44, -1.0, 1.0)
        calc.calcular_massa_soluto()