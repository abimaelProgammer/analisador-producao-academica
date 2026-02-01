import unicodedata
import string
from typing import Set

# Importe suas listas aqui ou cole-as
from .stopwords_pt import stopwords_pt
from .stopwords_en import stopwords_en

class ProcessadorTexto:
    def __init__(self):
        self.stop_words: Set[str] = set(stopwords_pt + stopwords_en)
    
    def normalizar(self, texto: str) -> str:
        """Remove acentos, pontuação e converte para minúsculas."""
        # Normalização Unicode (NFD) para separar acentos das letras
        texto_normalizado = unicodedata.normalize('NFD', texto)
        apenas_letras = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
        
        # Remove pontuação e converte para minúsculas
        tabela_traducao = str.maketrans('', '', string.punctuation + "¿¡")
        return apenas_letras.translate(tabela_traducao).lower()

    def extrair_palavras_validas(self, texto: str) -> list[str]:
        """Retorna lista de palavras limpas e filtradas (stopwords e tamanho > 3)."""
        texto_limpo = self.normalizar(texto)
        palavras = texto_limpo.split()
        return [p for p in palavras if len(p) > 3 and p not in self.stop_words]