# Projeto PNADC 2024 – Análise de Desigualdades Raciais

**Autor:** Felipe Geraldo de Oliveira  
**Matrícula:** 202310174  
**Etapa:** Desafio I (Filtro Inicial) do Zetta Lab 2025/2  
**Trilha:** Ciência e Governança de Dados
  

> **Observação:** Este projeto é exclusivo para a etapa do Zetta Lab 2025/2.

Este projeto teve como objetivo analisar os dados de 2024 da **PNADC (Pesquisa Nacional por Amostra de Domicílios Contínua)** do IBGE, com foco em **desigualdades raciais**.  

### **Escolha dos dados**
A PNADC fornece informações detalhadas sobre características socioeconômicas da população brasileira, como renda, escolaridade, acesso a serviços e auxílios. Esses dados permitem analisar **desigualdades entre grupos raciais**, que é o foco do projeto.

### **Metodologia de aquisição**
Os dados originais são obtidos diretamente do IBGE em formatos `.txt` e `.xls`. Para lidar com o tamanho e a complexidade dos arquivos:
- Foi criado o script `download_data.py` para baixar e organizar os arquivos brutos;

### **Principais passos do notebook**
O notebook `01_eda.ipynb` segue as etapas:
1. Carregamento e inspeção dos dados brutos;
2. Limpeza de inconsistências e padronização de variáveis;
3. Análise exploratória de dados (EDA) focada em desigualdades raciais;
4. Geração de gráficos e figuras para visualização de padrões socioeconômicos entre grupos raciais.

### **Principais insights da análise**
- Diferenças significativas de rendimento médio entre grupos raciais;
- Variações no acesso a serviços públicos e auxílios governamentais;
- Padrões de desigualdade que reforçam a necessidade de políticas públicas direcionadas.
---

## Estrutura de Pastas

```code
zetta-lab-desafio1
├── data
│   └── raw
├── notebooks
├── reports
│   └── figures
└── src
```

### **data**
Contém os arquivos de dados utilizados no projeto, organizados em duas subpastas:

- **raw/**: arquivos originais obtidos do IBGE (`.txt` e `.xls`).  
  **Nota:** atualmente está vazia, pois os arquivos originais são muito grandes (centenas de MB a GB). Para baixar e preparar os dados, execute `download_data.py` em `src/`.

- **processed/**: arquivos tratados após limpeza e transformação, em `.csv`.  
  **Nota:** também está vazia por enquanto; os arquivos são gerados ao rodar o notebook usando funções do módulo `process_data.py`.

### **notebooks**
Contém notebooks do projeto:

- `01_eda.ipynb`: notebook com limpeza e análise exploratória de dados (EDA), incluindo gráficos e estatísticas resumidas sobre desigualdades raciais. Utiliza funções do módulo `process_data.py`.

### **reports**
Contém outputs do projeto, como imagens e gráficos gerados durante a análise exploratória:

- **figures/**: visualizações comparando rendimento, escolaridade, acesso a serviços e auxílios entre grupos raciais.

### **src**
Contém scripts e módulos Python para baixar e processar os dados:

- `download_data.py`: script para download e preparação inicial dos dados brutos.  
- `process_data.py`: módulo com funções de limpeza, transformação e preparação dos dados, usadas pelo notebook.
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

- **Download dos dados:** após ativar o ambiente virtual e instalar os pacotes, execute o script `download_data.py` em `src/` para baixar e preparar os dados originais:

```bash
python src/download_data.py
```

- **Notebook:** depois de gerar os dados, abra e execute o notebook `01_eda.ipynb` em `notebooks/` para realizar a limpeza, transformação e análise exploratória.

```bash
jupyter notebook notebooks/01_eda.ipynb 
```
