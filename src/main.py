import schedule
import time
import pygame
import os
import logging
from datetime import datetime  # Importa datetime para capturar a data e hora

# Caminho do arquivo de áudio
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_FILE = os.path.join(BASE_DIR, "assets", "sino.mp3")

# Caminho do diretório de logs dentro do projeto
LOG_DIR = "/Users/lucasiqueira/Documents/Projects/angelus-sonus/logs"
LOG_FILE = os.path.join(LOG_DIR, "angelus-sonus.log")

# Criar diretório de logs se não existir
os.makedirs(LOG_DIR, exist_ok=True)

# Configuração do logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Exemplo de mensagem de log
logging.info("O script angelus-sonus foi iniciado com sucesso!")


def tocar_sino():
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Captura data e hora
    logging.info(f"🔔 Sino tocado em {agora}")  # Registra no log
    print(f"🔔 Tocando sino... ({agora})")  # Apenas para depuração manual
    pygame.mixer.init()
    pygame.mixer.music.load(AUDIO_FILE)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


# Agendar os horários
schedule.every().day.at("12:00").do(tocar_sino)
schedule.every().day.at("18:00").do(tocar_sino)


print("⏳ Alarme configurado! Aguardando horários...")

# Loop principal
while True:
    schedule.run_pending()
    time.sleep(30)  # Verifica o agendamento a cada 30 segundos
