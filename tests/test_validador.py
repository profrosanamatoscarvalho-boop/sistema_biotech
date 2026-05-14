# Arquivo: tests/test_validador.py
from validador import checar_secuencia_adn, calcular_conteudo_gc

def test_adn_totalmente_valido():
    assert checar_secuencia_adn("ATCG") == True

def test_adn_com_base_errada():
    assert checar_secuencia_adn("ATCX") == False

def test_calculo_gc_sucesso():
    # Numa sequencia de 4 letras com 2 G/C, o teor deve ser 50%
    assert calcular_conteudo_gc("ATCG") == 50.0