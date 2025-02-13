# Configuração do Angelus Sonus no Windows

Este documento explica como configurar e executar o Angelus Sonus no Windows.

## 1. Requisitos
Antes de iniciar, certifique-se de ter instalado:
- [Git](https://git-scm.com/download/win)
- [Python 3.11+](https://www.python.org/downloads/windows/)

## 2. Clonar o Repositório
Abra o Prompt de Comando ou PowerShell e execute:
```sh
cd C:\caminho\para\seu\diretorio
git clone https://github.com/lucasiqueira/angelus-sonus.git
cd angelus-sonus
```

## 3. Criar e Ativar Ambiente Virtual
```sh
python -m venv venv
venv\Scripts\activate
```

## 4. Instalar Dependências
```sh
pip install -r requirements.txt
```

## 5. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto e adicione:
```ini
PROJECT_PATH=C:\caminho\para\seu\diretorio\angelus-sonus
```

## 6. Testar a Execução Manualmente
```sh
python src\main.py
```
Se o sino tocar corretamente nos horários programados, a configuração está correta.

## 7. Configurar Execução Automática com o Agendador de Tarefas

1. Abra o **Agendador de Tarefas** do Windows.
2. Clique em **Criar Tarefa...**
3. Na aba **Geral**, defina um nome como `Angelus Sonus` e marque a opção **Executar com os privilégios mais altos**.
4. Na aba **Disparadores**, clique em **Novo...** e configure para iniciar a cada reinicialização ou em um horário específico.
5. Na aba **Ações**, clique em **Novo...**, escolha **Iniciar um programa** e em **Programa/script**, insira:
   ```sh
   C:\caminho\para\seu\diretorio\angelus-sonus\venv\Scripts\python.exe
   ```
6. No campo **Argumentos**, adicione:
   ```sh
   C:\caminho\para\seu\diretorio\angelus-sonus\src\main.py
   ```
7. Clique em **OK** e salve a tarefa.

Agora o script será executado automaticamente nos horários configurados.

## 8. Logs
Os logs são armazenados em `logs/angelus-sonus.log`. Para verificar os registros:
```sh
type logs\angelus-sonus.log
```

Se precisar de suporte, consulte o repositório oficial: [GitHub](https://github.com/lucasiqueira/angelus-sonus).

