import schedule
import time
import pygame
import os

# Caminho do arquivo de áudio
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_FILE = os.path.join(BASE_DIR, "assets", "sino.mp3")


def tocar_sino():
    print("🔔 Tocando sino...")
    pygame.mixer.init()
    pygame.mixer.music.load(AUDIO_FILE)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


# Agendar os horários
schedule.every().day.at("12:00").do(tocar_sino)
schedule.every().day.at("18:00").do(tocar_sino)

tocar_sino()
print("⏳ Alarme configurado! Aguardando horários...")

# Loop principal
while True:
    schedule.run_pending()
    time.sleep(30)  # Verifica o agendamento a cad


