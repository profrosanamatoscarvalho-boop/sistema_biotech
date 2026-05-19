import pytest
from app.validador import ValidadorSequencia

def test_sequencia_dna_valida():
    # Testa se reconhece uma fita de DNA correta
    validador = ValidadorSequencia("AATTCCGG")
    assert validador.possui_apenas_dna() is True

def test_sequencia_com_erro():
    # Testa se identifica letras que não pertencem ao DNA
    validador = ValidadorSequencia("AATTCXGG")
    assert validador.possui_apenas_dna() is False

def test_sequencia_vazia():
    # Testa o comportamento com campo vazio
    validador = ValidadorSequencia("")
    assert validador.possui_apenas_dna() is False