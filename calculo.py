def calcular_nota_final(m1, m2):
    """Calcula a nota final da faculdade, truncada para inteiro."""
    nota_final = (m1 + (m2 * 2)) / 3
    return int(nota_final)  # corta as casas decimais