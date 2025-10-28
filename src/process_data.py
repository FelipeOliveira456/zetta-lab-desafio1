import re
import pandas as pd
import os

def generate_pnadc_csv():
    """
    Processa arquivos PNADC Visita 1 específicos, lendo os arquivos
    de tamanho fixo em blocos e salvando em CSV.

    Todos os caminhos e arquivos estão fixos dentro da função.
    """
    input_dir = "../data/raw/"
    output_dir = "../data/processed"
    chunk_size = 10000  

    os.makedirs(output_dir, exist_ok=True)
    arquivos = [
        {
            "ano": 2024,
            "sas_file": "input_PNADC_2024_visita1_20250822.txt",
            "data_file": "PNADC_2024_visita1.txt"
        }
    ]

    for arq in arquivos:
        ano = arq["ano"]
        print(f"\n=== Processando PNADC {ano} Visita 1 ===")

        sas_file = os.path.join(input_dir, arq["sas_file"])
        with open(sas_file, "r", encoding="latin1") as f:
            sas_code = f.read()

        pattern = r"@(\d{4})\s+(\w+)\s+(\$?\d+)\."
        matches = re.findall(pattern, sas_code)

        colunas = []
        for inicio, nome, tipo in matches:
            if re.match(r"V1032\d{3}", nome): #pesos replicados
                continue
            inicio = int(inicio) - 1
            if tipo.startswith("$"):
                tamanho = int(tipo[1:])
                dtype = str
            else:
                tamanho = int(tipo)
                dtype = float
            fim = inicio + tamanho
            colunas.append({"nome": nome, "inicio": inicio, "fim": fim, "tipo": dtype})

        colspecs = [(col["inicio"], col["fim"]) for col in colunas]
        names = [col["nome"] for col in colunas]

        output_file = os.path.join(output_dir, f"PNADC_{ano}_visita1.csv")
        pd.DataFrame(columns=names).to_csv(output_file, index=False)

        input_data_file = os.path.join(input_dir, arq["data_file"])
        chunk_lines = []

        with open(input_data_file, "r", encoding="latin1") as f:
            for i, line in enumerate(f, 1):
                chunk_lines.append(line)
                if i % chunk_size == 0:
                    df_chunk = pd.DataFrame(
                        [[line[start:end].strip() for start, end in colspecs] for line in chunk_lines],
                        columns=names
                    )
                    for col in colunas:
                        df_chunk[col["nome"]] = df_chunk[col["nome"]].astype(col["tipo"], errors="ignore")
                    df_chunk.to_csv(output_file, index=False, mode="a", header=False, encoding="utf-8")
                    chunk_lines = []

            if chunk_lines:
                df_chunk = pd.DataFrame(
                    [[line[start:end].strip() for start, end in colspecs] for line in chunk_lines],
                    columns=names
                )
                for col in colunas:
                    df_chunk[col["nome"]] = df_chunk[col["nome"]].astype(col["tipo"], errors="ignore")
                df_chunk.to_csv(output_file, index=False, mode="a", header=False, encoding="utf-8")

        print(f"Arquivo {output_file} criado com sucesso!")

def read_pnadc_csv(ano=2024, visita=1, data_dir="../data/processed"):
    """
    Lê o CSV processado do PNADC em um DataFrame.

    Parâmetros:
    - ano: int, ano do arquivo PNADC
    - visita: int, número da visita (geralmente 1)
    - data_dir: diretório onde os CSVs processados estão salvos

    Retorna:
    - pandas.DataFrame
    """
    file_name = f"PNADC_{ano}_visita{visita}.csv"
    file_path = os.path.join(data_dir, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo {file_path} não existe. Execute primeiro a função de processamento.")

    df = pd.read_csv(file_path, encoding="utf-8")
    return df
    
def get_missing_values_percentage(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula e retorna a porcentagem de valores vazios (NaN) por coluna em um DataFrame.

    Retorna um DataFrame com duas colunas:
    - 'coluna': O nome da coluna.
    - 'pct_vazios': A porcentagem de valores ausentes (arredondada para 2 casas).
    
    A tabela retornada é filtrada para incluir apenas colunas com > 0% de vazios 
    e é ordenada de forma descendente pela porcentagem.

    Args:
        df (pd.DataFrame): O DataFrame de entrada.

    Returns:
        pd.DataFrame: A tabela de resumo de valores vazios.
    """
    
    # 1. Contar os valores nulos por coluna
    vazios_count = df.isnull().sum()
    
    # 2. Calcular a porcentagem de valores nulos
    total_linhas = len(df)
    vazios_percent = (vazios_count / total_linhas) * 100
    
    # 3. Criar o DataFrame de resumo
    tabela_vazios = pd.DataFrame({
        'coluna': df.columns,
        'pct_vazios': vazios_percent.values
    })
    
    # 4. Filtrar colunas que têm vazios (pct_vazios > 0)
    tabela_vazios_filtrada = tabela_vazios[tabela_vazios['pct_vazios'] > 0].copy()
    
    # 5. Arredondar a porcentagem
    tabela_vazios_filtrada['pct_vazios'] = tabela_vazios_filtrada['pct_vazios'].round(2)
    
    # 6. Ordenar pela porcentagem de forma descendente
    tabela_vazios_ordenada = tabela_vazios_filtrada.sort_values(
        by='pct_vazios',
        ascending=False
    ).reset_index(drop=True)
    
    return tabela_vazios_ordenada

def get_variables_for_nao_aplicavel(file_path, sheet_name=0):
    """
    Lê um arquivo XLS e retorna uma lista com os nomes das variáveis
    associadas aos valores 'Não aplicável'.
    
    Parâmetros:
    -----------
    file_path : str
        Caminho do arquivo XLS.
    sheet_name : int ou str, default 0
        Aba do Excel a ser lida.
    
    Retorna:
    --------
    list
        Lista de nomes/códigos de variáveis que têm pelo menos um 'Não aplicável'.
    """
    # Ler o arquivo
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='xlrd')

    variables = set()  # usar set para não repetir nomes

    for idx, row in df.iterrows():
        if str(row.get('Unnamed: 6')).strip().lower() in ('não aplicável', 'não se aplica', 'não ou não aplicável'):
            # Procurar valor correspondente na coluna Unnamed:2
            i = idx
            while pd.isna(df.at[i, 'Unnamed: 2']):
                i -= 1
            variables.add(df.at[i, 'Unnamed: 2'])

    return list(variables)

def fill_nao_aplicavel_with_zero(df, variables_with_nao_aplicavel):
    """
    Preenche com 0 os valores nulos das colunas listadas,
    considerando que 'Não aplicável' pode ser interpretado como nulo.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame a ser processado.
    variables_with_nao_aplicavel : list
        Lista de nomes de colunas que contêm valores 'Não aplicável'.

    Retorna:
    --------
    pd.DataFrame
        DataFrame com valores nulos preenchidos com 0 nas colunas indicadas.
    """
    for coluna in variables_with_nao_aplicavel:
        if coluna in df.columns:
            df[coluna] = df[coluna].fillna(0)
    return df




