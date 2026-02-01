import csv
import threading
from typing import List, Dict, Tuple
from .modelos import TrabalhoAcademico
from .processamento_texto import ProcessadorTexto

class AnalisadorDados:
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo
        self.trabalhos: List[TrabalhoAcademico] = []
        self.proc_texto = ProcessadorTexto()

    def carregar_dados(self):
        """Lê o CSV e popula a lista de objetos."""
        try:
            with open(self.caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
                leitor_csv = csv.reader(arquivo, delimiter=';')
                next(leitor_csv) # Pula cabeçalho
                for linha in leitor_csv:
                    # Mapeamento conforme seu código original
                    self.trabalhos.append(TrabalhoAcademico(
                        programa=linha[1],
                        orientador=linha[19],
                        grande_area=linha[24],
                        area=linha[25],
                        titulo=linha[5]
                    ))
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo não encontrado: {self.caminho_arquivo}")

    def gerar_ranking(self, atributo: str, top: int = 10) -> List[Tuple[str, int]]:
        """Gera ranking genérico baseado em um atributo do objeto."""
        contagem = {}
        # Uso de map conforme requisito funcional
        valores = map(lambda t: getattr(t, atributo), self.trabalhos)
        
        for v in valores:
            if v:
                contagem[v] = contagem.get(v, 0) + 1
        
        ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
        return ordenado[:top]

    def _worker_contagem(self, lista_trabalhos: List[TrabalhoAcademico], resultado: Dict):
        """Função interna executada por cada Thread."""
        local_count = {}
        for trabalho in lista_trabalhos:
            palavras = self.proc_texto.extrair_palavras_validas(trabalho.titulo)
            for p in palavras:
                local_count[p] = local_count.get(p, 0) + 1
        resultado.update(local_count)

    def ranking_palavras_concorrente(self, top: int = 20) -> List[Tuple[str, int]]:
        """Processa palavras mais frequentes usando Multithreading."""
        if not self.trabalhos:
            return []
            
        meio = len(self.trabalhos) // 2
        bloco1 = self.trabalhos[:meio]
        bloco2 = self.trabalhos[meio:]
        
        res1, res2 = {}, {}
        
        t1 = threading.Thread(target=self._worker_contagem, args=(bloco1, res1))
        t2 = threading.Thread(target=self._worker_contagem, args=(bloco2, res2))
        
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        # Merge dos resultados (Reduce)
        total = res1.copy()
        for k, v in res2.items():
            total[k] = total.get(k, 0) + v
            
        return sorted(total.items(), key=lambda x: x[1], reverse=True)[:top]