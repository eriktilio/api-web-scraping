import re
from difflib import SequenceMatcher


# Função para calcular a similaridade entre dois strings
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
