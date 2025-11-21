# Guia de Instalação do Python no Windows e MacOS

## Windows 11

### Antes do workshop

Instalação do Python 3.13 no Windows 11, com venv no VSCode

1. Download do VSCode a partir do site oficial: [code.visualstudio.com](https://code.visualstudio.com/).

2. Download do instalador do Python 3.13 na Windows store: [Python 3.13](https://apps.microsoft.com/detail/9pnrbtzxmb4z?hl=pt-PT&gl=PT).

3. Execute o instalador e siga as instruções.

### No workshop

1. Após a instalação, abra o Prompt de Comando (cmd) e verifique se o Python foi instalado corretamente executando:

```powershell
python --version
```

2. Para criar um ambiente virtual (venv), navegue até o diretório onde deseja criar o ambiente e execute:

```powershell
python -m venv .venv
```

3. Para ativar o ambiente virtual, execute:

```powershell
.venv\Scripts\activate
```

## MacOS

### Antes do workshop

Instalação de VSCode, homebrew e venv no MacOS

1. Download do VSCode a partir do site oficial: [code.visualstudio.com](https://code.visualstudio.com/).

### No workshop

1. Instalação do Homebrew, um gestor de pacotes para MacOS. Abra o Terminal e execute o seguinte comando:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Após a instalação do Homebrew, instale o Python 3.12 executando:

```bash
brew install python@3.13
```

3. Verifique se o Python foi instalado corretamente executando:

```bash
python3 --version
```

4. Para criar um ambiente virtual (venv), navegue até o diretório onde deseja criar o ambiente e execute:

```bash
python3 -m venv .venv
```

5. Para ativar o ambiente virtual, execute:

```bash
source .venv/bin/activate
```

## Instalar extensões no VSCode relacionadas com Python

1. Abra o VSCode e vá para a aba de extensões (ícone de quadrado no lado esquerdo ou `Ctrl+Shift+X`).
2. Procure por "Python" e instale a extensão oficial da Microsoft.
3. (Opcional) Instale outras extensões úteis, como "Pylance" para melhor suporte de linguagem.

## Instalação de pacotes

Com o ambiente virtual ativado, para instalar pacotes usando o pip:

```bash
pip install pandas
```

ou se existir um ficheiro `requirements.txt` com as dependências do projeto, pode-se instalar todas as dependências de uma vez:

```bash
pip install -r requirements.txt
```
