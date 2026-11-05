
#!/bin/bash

# Verifica se o usuário informou um diretório
if [ $# -ne 1 ]; then
    echo "Uso: ./executar.sh <diretorio>"
    exit 1
fi

DIRETORIO="$1"

# Executa o programa Python passando o diretório
python3 varredura.py "$DIRETORIO"
