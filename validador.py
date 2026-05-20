class ValidadorSequencia:
    """
    Sistema de checagem e integridade de amostras biologicas e fitas de acidos nucleicos.
    """

    def __init__(self, sequencia: str):
        self.seq = sequencia.strip().upper()

    def validar_rna(self) -> bool:
        """Verifica se a fita contem apenas as bases validas de RNA (A, U, C, G)."""
        if not self.seq:
            return False
        bases_rna = {'A', 'U', 'C', 'G'}
        return set(self.seq).issubset(bases_rna)

    def validar_dna(self) -> bool:
        """Verifica se a fita contem apenas as bases validas de DNA (A, T, C, G)."""
        if not self.seq:
            return False
        bases_dna = {'A', 'T', 'C', 'G'}
        return set(self.seq).issubset(bases_dna)
