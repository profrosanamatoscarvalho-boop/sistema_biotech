# Arquivo: tests/test_validador.py
from validador import checar_secuencia_adn

def test_adn_totalmente_valido():
    # Teste com uma sequencia correta
    assert checar_secuencia_adn("ATCG") == True

def test_adn_com_base_errada():
    # Teste com a letra X que nao existe no DNA
    assert checar_secuencia_adn("ATCX") == False