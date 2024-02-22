def substituir_bytes(nome_arquivo, offset, novos_bytes):
    with open(nome_arquivo, 'r+b') as arquivo:
        arquivo.seek(offset)
        arquivo.write(novos_bytes)

# Nome do arquivo a ser editado
nome_arquivo = input("File: ")

# Offset onde a substituição será feita (44 e 45 para 00 00)
offset = 0x00000044

# Novos bytes a serem escritos
novos_bytes = b'\x00\x00'

# Chama a função para substituir os bytes
substituir_bytes(nome_arquivo, offset, novos_bytes)

print("Substituição concluída com sucesso!")
