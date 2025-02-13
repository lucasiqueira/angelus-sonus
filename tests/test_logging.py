import os

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs")
LOG_FILE = os.path.join(LOG_DIR, "angelus-sonus.log")


def test_log_directory_exists():
    """Verifica se o diretório de logs existe"""
    assert os.path.exists(LOG_DIR), "O diretório de logs não foi encontrado!"


def test_log_file_exists():
    """Verifica se o arquivo de log foi criado"""
    assert os.path.exists(LOG_FILE), (
        "O arquivo de log angelus-sonus.log não foi encontrado!"
    )


def test_log_is_written():
    """Verifica se há pelo menos uma entrada no log"""
    with open(LOG_FILE, "r") as log:
        lines = log.readlines()
    assert len(lines) > 0, "O arquivo de log está vazio!"
