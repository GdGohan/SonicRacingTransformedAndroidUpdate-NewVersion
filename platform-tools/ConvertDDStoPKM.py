import struct
import os

def dds_to_pkm(dds_file_name):
    dds_file_path = f"{dds_file_name}.dds"

    # Verifique se o arquivo DDS existe
    if not os.path.exists(dds_file_path):
        print(f"Arquivo não encontrado: {dds_file_path}")
        return

    # Abrir arquivo DDS para leitura em modo binário
    with open(dds_file_path, 'rb') as dds_file:
        # Ler o arquivo DDS completo
        dds_data = dds_file.read()
        
        # Extrair altura e largura do DDS (assumindo que estão nos bytes 12 a 19)
        height, width = struct.unpack_from('II', dds_data, 12)

    # Criar cabeçalho PKM com a altura e largura extraídas
    pkm_header = struct.pack('>4sHHHHHH', b'PKM ', 0x3130, 0x0000, width, height, width, height)
    
    # Preparar o conteúdo PKM (cabeçalho PKM + restante do DDS sem o cabeçalho original)
    pkm_content = pkm_header + dds_data[128:]  # Supondo que o cabeçalho DDS ocupe 128 bytes

    # Salvar o conteúdo PKM em um novo arquivo
    pkm_file_path = f"{dds_file_name}.pkm"
    with open(pkm_file_path, 'wb') as pkm_file:
        pkm_file.write(pkm_content)
    
    print(f"Arquivo PKM salvo como: {pkm_file_path}")

# Solicitar ao usuário para digitar o nome do arquivo DDS (sem extensão)
dds_file_name = input("file name: ")

# Executar a função com o nome do arquivo fornecido
dds_to_pkm(dds_file_name)
