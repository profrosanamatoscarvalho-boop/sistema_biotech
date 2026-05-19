class ValidadorSequencia:
    """
    Classe para validação básica de integridade de fitas de ácidos nucleicos.
    """
    def __init__(self, sequencia: str):
        self.sequencia = sequencia.strip().upper()

    def possui_apenas_dna(self) -> bool:
        """Verifica se a sequência contém apenas as bases A, T, C, G."""
        if not self.sequencia:
            return False
        return set(self.sequencia).issubset({'A', 'T', 'C', 'G'})