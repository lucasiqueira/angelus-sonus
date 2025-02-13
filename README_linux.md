# Guia de Configuração do Angelus Sonus no Linux

Este guia explica como configurar e executar o projeto Angelus Sonus em um ambiente Linux.

## Requisitos
- Python 3.11+
- `pip` instalado
- `virtualenv` instalado
- `systemd` para automação

## Passo a Passo

### 1. Clonar o Repositório
```bash
git clone https://github.com/lucasiqueira/angelus-sonus.git
cd angelus-sonus
```

### 2. Criar e Ativar o Ambiente Virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Criar o Arquivo `.env`
Crie um arquivo `.env` na raiz do projeto e adicione:
```bash
PROJECT_PATH=/caminho/para/angelus-sonus
```
Substitua `/caminho/para/angelus-sonus` pelo caminho correto do projeto.

### 5. Testar a Execução Manualmente
```bash
python src/main.py
```

Se tudo estiver certo, o sino tocará conforme o agendamento.

### 6. Configurar a Execução Automática com systemd
Crie um arquivo de serviço systemd:
```bash
nano ~/.config/systemd/user/angelus-sonus.service
```
E adicione:
```ini
[Unit]
Description=Angelus Sonus - Alarme de Sino
After=network.target

[Service]
WorkingDirectory=/caminho/para/angelus-sonus
ExecStart=/caminho/para/angelus-sonus/venv/bin/python /caminho/para/angelus-sonus/src/main.py
Restart=always
User=seu_usuario

[Install]
WantedBy=default.target
```
Substitua `/caminho/para/angelus-sonus` pelo caminho correto e `seu_usuario` pelo seu nome de usuário.

### 7. Iniciar e Ativar o Serviço
```bash
systemctl --user daemon-reload
systemctl --user start angelus-sonus.service
systemctl --user enable angelus-sonus.service
```

Agora, o script será executado automaticamente nos horários configurados.

## Logs
Os logs serão armazenados na pasta `logs` dentro do diretório do projeto.

```bash
tail -f logs/angelus-sonus.log
```

## Solução de Problemas
- Se o serviço não iniciar, use `journalctl --user -xe -u angelus-sonus` para verificar os erros.
- Certifique-se de que `systemd` está configurado corretamente e de que o caminho do Python está correto.

