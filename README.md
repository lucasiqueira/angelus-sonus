# Angelus Sonus

Angelus Sonus é uma aplicação em Python que toca um sino automaticamente todos os dias às 12:00 PM e às 6:00 PM. A execução é automatizada no macOS utilizando `launchctl` e todas as atividades são registradas em um arquivo de log.

## Funcionalidades
- Toca um sino nos horários predefinidos (12:00 e 18:00).
- Registra logs de eventos da aplicação.
- Suporte para agendamento automático via `launchctl` no macOS.

## Requisitos
- macOS
- Python 3.8+
- `pygame` para reproduzir o som do sino
- `schedule` para gerenciar os horários

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/lucasiqueira/angelus-sonus.git
cd angelus-sonus
```

### 2. Criar um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
touch .env
```
E adicione a seguinte linha:

```ini
PROJECT_PATH=/Users/lucasiqueira/Documents/Projects
```

### 5. Executar o script manualmente

```bash
python src/main.py
```

Se tudo estiver correto, o sino tocará imediatamente para teste e o agendamento será iniciado.

## Automatização no macOS com LaunchAgent

Para que o script rode automaticamente, criamos um arquivo de configuração `LaunchAgent`.

### 1. Criar o arquivo de agente
Crie um arquivo `com.angelus.sonus.plist` dentro do diretório `~/Library/LaunchAgents/`:

```bash
touch ~/Library/LaunchAgents/com.angelus.sonus.plist
```

### 2. Adicionar a configuração ao arquivo
Edite o arquivo com o seguinte conteúdo (substituindo `USERNAME` pelo seu usuário):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.angelus.sonus</string>
        <key>ProgramArguments</key>
        <array>
            <string>/Users/USERNAME/Documents/Projects/angelus-sonus/venv/bin/python3</string>
            <string>/Users/USERNAME/Documents/Projects/angelus-sonus/src/main.py</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
        <key>KeepAlive</key>
        <true/>
        <key>StandardOutPath</key>
        <string>/Users/USERNAME/Documents/Projects/angelus-sonus/logs/output.log</string>
        <key>StandardErrorPath</key>
        <string>/Users/USERNAME/Documents/Projects/angelus-sonus/logs/error.log</string>
    </dict>
</plist>
```

### 3. Carregar o agente

```bash
launchctl load ~/Library/LaunchAgents/com.angelus.sonus.plist
```

Para garantir que o agente esteja rodando:

```bash
launchctl list | grep angelus.sonus
```

Se precisar recarregar:

```bash
launchctl unload ~/Library/LaunchAgents/com.angelus.sonus.plist
launchctl load ~/Library/LaunchAgents/com.angelus.sonus.plist
```

### 4. Testar se está funcionando

Se desejar testar sem esperar pelos horários configurados, altere `main.py` para usar um horário próximo:

```python
schedule.every().day.at("12:05").do(tocar_sino)
```

Ou execute o script diretamente para ver se funciona:

```bash
python src/main.py
```

## Logs

Todos os logs são armazenados no diretório `logs/` dentro do projeto. O arquivo de log principal é `angelus-sonus.log`.

Para visualizar os logs:

```bash
tail -f logs/angelus-sonus.log
```

Caso o script seja interrompido manualmente (`Ctrl+C`), será registrado um aviso no log.

## Contribuição

Sinta-se à vontade para abrir issues e pull requests no repositório do GitHub!

## Licença

Lucas Siqueira - 2025

