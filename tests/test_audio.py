import os
import pygame

AUDIO_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "../src/assets/sino.mp3"
)


def test_audio_file_exists():
    """Verifica se o arquivo de áudio do sino existe"""
    assert os.path.exists(AUDIO_PATH), "O arquivo sino.mp3 não foi encontrado!"


def test_audio_can_play():
    """Verifica se o áudio pode ser carregado e reproduzido sem erros"""
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(AUDIO_PATH)
        assert True  # Se não houver erro, o teste passa
    except pygame.error as e:
        assert False, f"Erro ao carregar o áudio: {e}"
