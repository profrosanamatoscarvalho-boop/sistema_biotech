class CalculadoraMolaridade:
    """
    Classe para automação de cálculos de preparo de soluções em laboratórios de biotecnologia,
    determinando a massa de soluto necessária para atingir uma dada molaridade.
    """

    def __init__(self, massa_molar: float, volume_litros: float, molaridade_desejada: float):
        self.massa_molar = massa_molar
        self.volume_litros = volume_litros
        self.molaridade_desejada = molaridade_desejada

    def calcular_massa_soluto(self) -> float:
        """
        Calcula a massa necessária em gramas.
        Fórmula clássica: Massa (g) = Molaridade (mol/L) * Volume (L) * Massa Molar (g/mol)
        """
        if self.massa_molar <= 0 or self.volume_litros <= 0 or self.molaridade_desejada <= 0:
            raise ValueError("Todos os parâmetros químicos devem ser maiores do que zero.")
        
        massa_g = self.molaridade_desejada * self.volume_litros * self.massa_molar
        return round(massa_g, 2)