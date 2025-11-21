# Guia para o Terminal (bash/zsh e powershell)

## navegar em diretórios

- `ls` : lista os ficheiros e pastas no diretório atual (equivalente a `dir` no Windows)
- `cd nome_da_pasta` : entra na pasta especificada
- `cd ..` : sobe um nível na hierarquia de pastas

## pastas

- `mkdir nome_da_pasta` : cria uma nova pasta com o nome especificado
- `rmdir nome_da_pasta` : remove a pasta especificada (deve estar vazia)

## ficheiros

- `touch nome_do_ficheiro` : cria um novo ficheiro vazio com o nome especificado
- `rm nome_do_ficheiro` : remove o ficheiro especificado

## Git

- `git clone url_do_repositorio` : clona um repositório remoto
- `git init` : inicializa um novo repositório Git local
- `git add nome_do_ficheiro` : adiciona o ficheiro especificado à área de staging
- `git commit -m "mensagem do commit"` : cria um commit com a mensagem especificada
- `git push origin nome_da_branch` : envia os commits locais para o repositório remoto na branch especificada
- `git pull origin nome_da_branch` : puxa as alterações do repositório remoto para a branch local especificada

## Ambiente virtual Python

- `python --version` ou `python3 --version` : verifica a versão do Python instalada
- `python -m venv .venv` ou `python3 -m venv .venv` : cria um ambiente virtual com o nome `.venv`
- `source .venv/bin/activate` : ativa o ambiente virtual (MacOS/Linux)
- `.venv\Scripts\activate` : ativa o ambiente virtual (Windows)
- `deactivate` : sai do ambiente virtual (MacOS/Linux/Windows)

## executar scripts Python

- `python nome_do_ficheiro.py` ou `python3 nome_do_ficheiro.py` : executa o ficheiro Python especificado

## pip (gestor de pacotes Python)

- `pip install nome_do_pacote` : instala um pacote Python no ambiente virtual
- `pip freeze > requirements.txt` : cria um ficheiro com a lista de pacotes instalados
- `pip install -r requirements.txt` : instala os pacotes listados no ficheiro requirements.txt

## Streamlit

- `streamlit run nome_do_ficheiro.py` : executa uma aplicação Streamlit a partir do ficheiro Python especificado

## outros comandos úteis

- `Ctrl + C` : interrompe a execução do programa atual no terminal
- `clear` : limpa a tela do terminal (equivalente a `cls` no Windows)
- `cat nome_do_ficheiro` : exibe o conteúdo do ficheiro especificado no terminal
- `nano nome_do_ficheiro` : abre o ficheiro especificado no editor de texto nano (MacOS/Linux)
