import schedule
import time
import pygame
import os
import logging
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Definir caminhos do projeto usando a variável do .env
PROJECT_PATH = os.getenv("PROJECT_PATH")
LOG_DIR = os.path.join(PROJECT_PATH, "angelus-sonus/logs")

# Caminho do arquivo de áudio
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_FILE = os.path.join(BASE_DIR, "assets", "sino.mp3")

# Caminho do arquivo de log
LOG_FILE = os.path.join(LOG_DIR, "angelus-sonus.log")

# Criar diretório de logs se não existir
os.makedirs(LOG_DIR, exist_ok=True)

# Configuração do logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("O script angelus-sonus foi iniciado com sucesso!")


def tocar_sino():
    logging.info("🔔 Sino tocado")
    print("🔔 Tocando sino...")
    pygame.mixer.init()
    pygame.mixer.music.load(AUDIO_FILE)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    logging.info("🔔 Sino finalizado")


def iniciar_aplicacao():
    logging.info("📌 Iniciando aplicação...")
    print("📌 Iniciando aplicação...")
    print("🔔 Testando execução do sino...")
    tocar_sino()
    print("🔔 Teste concluído com sucesso!")
    logging.info("📌 Aplicação iniciada com sucesso.")
    logging.info("⏳ Alarme configurado! Aguardando horários...")


iniciar_aplicacao()

# Agendar os horários
schedule.every().day.at("12:00").do(tocar_sino)
schedule.every().day.at("18:00").do(tocar_sino)

try:
    print("⏳ Alarme configurado! Aguardando horários...")
    while True:
        schedule.run_pending()
        time.sleep(30)

except KeyboardInterrupt:
    logging.warning("⚠️ Script interrompido pelo usuário (Ctrl+C).")
    print("\n⚠️ Interrupção detectada! Encerrando script com segurança.")

except Exception as e:
    logging.error(f"❌ Erro inesperado: {e}")
    print(f"\n❌ Erro inesperado: {e}")

finally:
    logging.info("📌 Script angelus-sonus finalizado.")
    print("📌 Script encerrado.")
