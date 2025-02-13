import schedule
import time
import pygame
import os
import logging
import sys
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Definir caminho base do projeto
PROJECT_PATH = os.getenv(
    "PROJECT_PATH",
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

# Definir caminho da pasta de logs e arquivo de log
LOG_DIR = os.path.join(PROJECT_PATH, "logs")
LOG_FILE = os.path.join(LOG_DIR, "angelus-sonus.log")

# Criar diretório de logs se não existir
os.makedirs(LOG_DIR, exist_ok=True)

# Criar handlers separados para stdout e stderr
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)  # INFO, DEBUG e WARNING

stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.ERROR)  # Apenas ERROR e CRITICAL

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        stdout_handler,
        stderr_handler
    ],
)

logging.info("📌 O script angelus-sonus foi iniciado com sucesso!")

# Caminho do arquivo de áudio
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_FILE = os.path.join(BASE_DIR, "assets", "sino.mp3")


def suprimir_saida_pygame():
    """Função para suprimir a saída do pygame."""
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(AUDIO_FILE)
            pygame.mixer.music.play()
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr


def tocar_sino():
    logging.info("🔔 Sino tocado")

    while pygame.mixer.music.get_busy():
        time.sleep(1)

    logging.info("🔔 Sino finalizado")


def iniciar_aplicacao():
    suprimir_saida_pygame()
    logging.info("📌 Iniciando aplicação...")
    tocar_sino()
    logging.info("📌 Aplicação iniciada com sucesso.")
    logging.info("⏳ Alarme configurado! Aguardando horários...")


iniciar_aplicacao()

# Agendar os horários
schedule.every().day.at("12:00").do(tocar_sino)
schedule.every().day.at("18:00").do(tocar_sino)

try:
    while True:
        schedule.run_pending()
        time.sleep(30)

except KeyboardInterrupt:
    logging.warning("⚠️ Script interrompido pelo usuário (Ctrl+C).")

except Exception as e:
    logging.error(f"❌ Erro inesperado: {e}")

finally:
    logging.info("📌 Script angelus-sonus finalizado.")
