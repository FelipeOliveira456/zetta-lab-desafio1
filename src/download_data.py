import os
from ftplib import FTP
import zipfile

def baixar_pnadc_2024(BASE_DIR):
    FTP_HOST = 'ftp.ibge.gov.br'
    FTP_DIR_DADOS = '/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/'
    FTP_DIR_DOCS = '/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/'

    os.makedirs(BASE_DIR, exist_ok=True)

    arquivos = {
        'Dados': ["PNADC_2024_visita1_20250822.zip"],
        'Documentacao': [
            "input_PNADC_2024_visita1_20250822.txt",
            "dicionario_PNADC_microdados_2024_visita1_20250822.xls"
        ]
    }

    ftp = FTP(FTP_HOST)
    ftp.login('anonymous', 'anonymous@example.com')

    # === Baixar dados ===
    ftp.cwd(FTP_DIR_DADOS)
    for nome in arquivos['Dados']:
        local_path = os.path.join(BASE_DIR, nome)
        print(f"Baixando {nome} …")
        with open(local_path, 'wb') as f:
            ftp.retrbinary('RETR ' + nome, f.write)
        print(f"{nome} baixado com sucesso.")

        # Extrair ZIP e remover
        if nome.endswith(".zip"):
            with zipfile.ZipFile(local_path, 'r') as z:
                z.extractall(BASE_DIR)
            os.remove(local_path)
            print(f"{nome} extraído e removido.")

    # === Baixar documentação ===
    ftp.cwd(FTP_DIR_DOCS)
    for nome in arquivos['Documentacao']:
        local_path = os.path.join(BASE_DIR, nome)
        print(f"Baixando {nome} …")
        with open(local_path, 'wb') as f:
            ftp.retrbinary('RETR ' + nome, f.write)
        print(f"{nome} baixado com sucesso.")

    ftp.quit()
    print("Download PNADC 2024 concluído!")

if __name__ == "__main__":
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/raw"))
    baixar_pnadc_2024(BASE_DIR)

