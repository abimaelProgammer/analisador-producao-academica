import argparse
import sys
from src.pipeline import AnalisadorDados

def imprimir_relatorio(titulo: str, dados: list):
    print(f"\n--- {titulo} ---")
    for i, (chave, valor) in enumerate(dados, 1):
        print(f"{i}º - {chave}: {valor}")
    print("-" * 30)

def main():
    parser = argparse.ArgumentParser(description="Analisador de Produção Acadêmica CAPES")
    parser.add_argument("arquivo", help="Caminho para o arquivo .csv")
    args = parser.parse_args()

    print(f"Iniciando processamento de: {args.arquivo}...")
    
    try:
        analisador = AnalisadorDados(args.arquivo)
        analisador.carregar_dados()
        
        print("Dados carregados. Gerando métricas...")

        # Rankings
        imprimir_relatorio("Top 10 Orientadores", analisador.gerar_ranking('orientador'))
        imprimir_relatorio("Top 10 Programas", analisador.gerar_ranking('programa'))
        
        print("\nCalculando frequência de palavras (Multithreading)...")
        palavras = analisador.ranking_palavras_concorrente()
        imprimir_relatorio("Top 20 Palavras em Títulos", palavras)

    except Exception as e:
        print(f"Erro Crítico: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()