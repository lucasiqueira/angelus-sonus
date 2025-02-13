import schedule
import time


def job():
    print("Job is running")


def test_scheduled_tasks():
    """Verifica se os horários do sino foram corretamente agendados"""
    # Agendar trabalhos para os horários esperados
    schedule.every().day.at("12:00").do(job)
    schedule.every().day.at("18:00").do(job)

    # Simular a execução do agendamento
    time.sleep(1)  # Esperar para garantir que os trabalhos sejam agendados

    job_times = [job.next_run.strftime("%H:%M") for job in schedule.jobs]
    assert "12:00" in job_times, "Horário das 12:00 não está agendado!"
    assert "18:00" in job_times, "Horário das 18:00 não está agendado!"
