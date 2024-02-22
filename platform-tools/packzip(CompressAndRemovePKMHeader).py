import struct
import os
import subprocess

def remove_pkm_header(pkm_file_name):
    pkm_file_path = f"{pkm_file_name}"

    # Verifique se o arquivo PKM existe
    if not os.path.exists(pkm_file_path):
        print(f"Arquivo não encontrado: {pkm_file_path}")
        return

    # Abrir arquivo PKM para leitura em modo binário
    with open(pkm_file_path, 'rb') as pkm_file:
        # Ler o arquivo PKM completo
        pkm_data = pkm_file.read()
        pkm_content = pkm_data
        pkm_file.seek(0)
        pkm_header = pkm_file.read(3)
        
        # Remover o cabeçalho PKM (10 bytes)
        if pkm_header == b'PKM':
             pkm_content = pkm_data[16:]

    # Salvar o conteúdo PKM sem o cabeçalho em um novo arquivo .dat
    dat_file_path = f"{pkm_file_name}.dat"
    with open(dat_file_path, 'wb') as dat_file:
        dat_file.write(pkm_content)
    
    print(f"Arquivo .dat salvo como: {dat_file_path}")
    return dat_file_path

def packzip_command(dat_file_path, stz_file_name, offset):
    # Construir o comando packzip
    command = f"packzip -o {offset} {dat_file_path} {stz_file_name}"

    # Executar o comando usando subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        print("Comando executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")

def main():
    # Solicitar ao usuário para digitar o nome do arquivo PKM (sem extensão)
    pkm_file_name = input("PKM File: ")

    # Remover o cabeçalho PKM e obter o nome do arquivo .dat resultante
    dat_file_path = remove_pkm_header(pkm_file_name)

    if dat_file_path:
        # Solicitar ao usuário para digitar o nome do arquivo .stz
        stz_file_name = input("stz File: ")
        
        # Solicitar ao usuário para digitar o offset
        offset = input("offset (PKM ID): ")
        
        offset = "0x" + offset

        # Executar o comando packzip
        packzip_command(dat_file_path, stz_file_name, offset)

if __name__ == "__main__":
    main()
