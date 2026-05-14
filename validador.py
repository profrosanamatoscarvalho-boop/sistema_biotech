# Archivo: validador.py

def checar_secuencia_adn(sequencia):
    """Verifica se a sequencia contem apenas bases validas (A, T, C, G)"""
    if not sequencia:
        return False
    
    # Passamos para maiusculo para evitar erros de digitacao
    sequencia = sequencia.upper()
    bases_validas = {'A', 'T', 'C', 'G'}
    
    for base in sequencia:
        if base not in bases_validas:
            return False
    return True