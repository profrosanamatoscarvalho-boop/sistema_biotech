# Archivo: validador.py

def checar_secuencia_adn(sequencia):
    """Verifica se a sequencia contem apenas bases validas (A, T, C, G)"""
    if not sequencia:
        return False
    
    sequencia = sequencia.upper()
    bases_validas = {'A', 'T', 'C', 'G'}
    
    for base in sequencia:
        if base not in bases_validas:
            return False
    return True

def calcular_conteudo_gc(sequencia):
    """Calcula a porcentagem de bases G e C na sequencia de DNA"""
    # BUG PROPOSITAL: Se a sequencia for vazia, vai quebrar aqui!
    sequencia = sequencia.upper()
    g_count = sequencia.count('G')
    c_count = sequencia.count('C')
    
    porcentagem = ((g_count + c_count) / len(sequencia)) * 100
    return porcentagem