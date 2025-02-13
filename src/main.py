import schedule
import time
import pygame
import os
import logging

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
    logging.info("🔔 Sino tocado")  # Registra no log
    print("🔔 Tocando sino...")  # Apenas para depuração manual
    pygame.mixer.init()
    pygame.mixer.music.load(AUDIO_FILE)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    logging.info("🔔 Sino finalizado")  # Registra no log


def iniciar_aplicacao():
    logging.info("📌 Iniciando aplicação...")
    print("📌 Iniciando aplicação...")
    print("🔔 Testando execução do sino...")
    tocar_sino()
    print("🔔 Teste concluído com sucesso!")
    logging.info("📌 Aplicação iniciada com sucesso.")


iniciar_aplicacao()

# Agendar os horários
schedule.every().day.at("12:00").do(tocar_sino)
schedule.every().day.at("18:00").do(tocar_sino)

try:
    print("⏳ Alarme configurado! Aguardando horários...")
    while True:
        schedule.run_pending()
        time.sleep(30)  # Verifica o agendamento a cada 30 segundos

except KeyboardInterrupt:
    logging.warning("⚠️ Script interrompido pelo usuário (Ctrl+C).")
    print("\n⚠️ Interrupção detectada! Encerrando script com segurança.")

except Exception as e:
    logging.error(f"❌ Erro inesperado: {e}")
    print(f"\n❌ Erro inesperado: {e}")

finally:
    logging.info("📌 Script angelus-sonus finalizado.")
    print("📌 Script encerrado.")
