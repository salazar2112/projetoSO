import os
import sys
import hashlib

# Verifica se o caminho foi informado
if len(sys.argv) != 2:
    print("Uso: ./executar.sh <diretorio>")
    sys.exit(1)

diretorio = sys.argv[1]

# Verifica se o diretório existe
if not os.path.isdir(diretorio):
    print("Erro: diretório inválido ou inexistente.")
    sys.exit(1)


# Calcula o hash SHA-256 de um arquivo
def calcular_hash(caminho):
    sha256 = hashlib.sha256()

    with open(caminho, "rb") as arquivo:
        while True:
            bloco = arquivo.read(4096)

            if not bloco:
                break

            sha256.update(bloco)

    return sha256.hexdigest()


# Estrutura que armazenará os arquivos e seus hashes
arquivos_hash = {}

print(f"Iniciando varredura em: {diretorio}")

# Varredura recursiva
for raiz, diretorios, arquivos in os.walk(diretorio):

    for nome_arquivo in arquivos:

        caminho_completo = os.path.join(raiz, nome_arquivo)

        try:
            hash_arquivo = calcular_hash(caminho_completo)

            # Atualiza a estrutura com o caminho e o hash
            arquivos_hash[caminho_completo] = hash_arquivo

            print(f"\nArquivo: {caminho_completo}")
            print(f"SHA-256: {hash_arquivo}")

        except OSError as erro:
            print(f"Erro ao acessar {caminho_completo}: {erro}")


# Resultado final
print("\n========== RESULTADO ==========")
print(f"Total de arquivos processados: {len(arquivos_hash)}")
print(f"Total de hashes armazenados: {len(arquivos_hash)}")
