import pytest
from validador import ValidadorSequencia

def test_validar_rna_valido():
    validador = ValidadorSequencia("AUGCCG")
    assert validador.validar_rna() is True

def test_validar_dna_valido():
    validador = ValidadorSequencia("ATGCCG")
    assert validador.validar_dna() is True
