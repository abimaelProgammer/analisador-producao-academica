# Analisador de Produção Acadêmica (CAPES Data Pipeline) 📊

Este projeto consiste em um pipeline de engenharia de dados desenvolvido em Python para processar grandes volumes de registros acadêmicos (datasets da CAPES).

O sistema realiza ingestão de dados, normalização de texto e extração de insights estatísticos, utilizando técnicas de **Programação Concorrente** para otimização de performance.

## 🚀 Destaques Técnicos

* **Multithreading:** Processamento paralelo de texto utilizando a biblioteca `threading`, dividindo a carga de trabalho de tokenização e contagem de palavras (MapReduce simplificado).
* **Programação Funcional:** Utilização extensiva de `map`, `filter`, expressões lambda e list comprehensions para manipulação de dados.
* **Text Mining:** Pipeline de limpeza (NLP básico) com normalização Unicode, remoção de stopwords (PT/EN) e pontuação.
* **Arquitetura Modular:** Separação clara entre Modelos, Lógica de Negócio e Interface CLI.

## 📂 Estrutura do Projeto

```text
analisador-producao-academica/
├── src/
│   ├── modelos.py             # Definição de Data Classes
│   ├── pipeline.py            # Lógica de ingestão e concorrência
│   └── processamento_texto.py # Normalização e Stopwords
├── data/                      # Diretório para datasets (.csv)
├── main.py                    # Entry point da CLI
└── README.md

⚙️ Como Executar
Certifique-se de ter o Python 3 instalado.

1. Coloque o ficheiro de dados (ex: ap2-capes-ufc-2021.csv) na pasta data/.

2. Execute o comando no terminal:
# Exemplo de execução
python main.py data/ap2-capes-ufc-2021.csv