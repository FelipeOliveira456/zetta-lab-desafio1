# Projeto PNADC 2024 – Análise de Desigualdades Raciais

**Autor:** Felipe Geraldo de Oliveira  
**Etapa:** Desafio I (Filtro Inicial) do Zetta Lab 2025/2  
**Trilha:** Ciência e Governança de Dados  

Este projeto teve como objetivo analisar os dados de 2024 da **PNADC (Pesquisa Nacional por Amostra de Domicílios Contínua)** do IBGE, com foco em **desigualdades raciais**. Foram realizadas **análises exploratórias de dados** e limpeza das bases, produzindo um conjunto de dados tratados e visualizações para apoiar a análise.

---

## Estrutura de Pastas

zetta-lab-desafio1
├── data
│   └── raw
├── notebooks
├── reports
│   └── figures
└── src

### **data**
Contém os arquivos de dados utilizados no projeto, organizados em duas subpastas:

- **raw/**: arquivos originais obtidos do IBGE, em formatos `.txt` e `.xls`.  
  **Obs:** atualmente esta pasta não contém nenhum dado, pois os arquivos originais são grandes. Para baixar e preparar os dados, é necessário executar o script `download_data.py` presente em `src/`.
  
- **processed/**: arquivos tratados após a limpeza e transformação, prontos para análise exploratória. Aqui estão os dados limpos e consolidados, em formato `.csv`.

### **notebooks**
Contém notebooks do projeto, sendo:
- `01_eda.ipynb`: notebook com limpeza e análise exploratória de dados (EDA), incluindo gráficos e estatísticas resumidas focadas em desigualdades raciais.

### **reports**
Contém outputs do projeto, como imagens e gráficos gerados durante a análise exploratória:
- **figures/**: imagens de visualizações, como comparações de rendimento, escolaridade, acesso a serviços e auxílios entre grupos raciais.

### **src**
Contém os scripts Python utilizados para baixar e processar os dados:
- `download_data.py`: script para download e preparação inicial dos dados.
- `process_data.py`: script para limpeza, transformação e preparação dos dados para análise.zetta-lab-desafio1

---

## Requisitos e Ambiente

- **Python recomendado:** 3.11.14  
  > Versões mais recentes (Python 3.12+) ainda não têm todas as bibliotecas utilizadas totalmente compatíveis.  

- É recomendado criar um **ambiente virtual (venv)** antes de instalar os pacotes:

```bash
python3.11 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

