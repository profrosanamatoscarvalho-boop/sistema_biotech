class CalculadoraBiotech:
    """
    Ferramenta para calculos basicos de laboratorio, preparo de solucoes
    e fatores de diluicao moleculares.
    """

    @staticmethod
    def calcular_diluicao(concentracao_inicial: float, volume_inicial: float, concentracao_final: float) -> float:
        """Calcula o volume final necessario para uma diluicao (C1V1 = C2V2)."""
        if concentracao_inicial <= 0 or volume_inicial <= 0 or concentracao_final <= 0:
            raise ValueError("Os valores de concentracao e volume devem ser maiores que zero.")
        
        # Formula classica: V2 = (C1 * V1) / C2
        volume_final = (concentracao_inicial * volume_inicial) / concentracao_final
        return round(volume_final, 2)

    @staticmethod
    def calcular_massa_molar(mols: float, massa_molecular: float) -> float:
        """Calcula a massa necessaria em gramas (m = n * MM)."""
        if mols <= 0 or massa_molecular <= 0:
            raise ValueError("Quantidade de mols e massa molecular devem ser positivas.")
        return round(mols * massa_molecular, 2)
