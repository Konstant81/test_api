import logging
from celery.utils.log import get_task_logger
from django.utils.timezone import now
from django.db.models import Q
from api.celery import app
import sender.models


my_logger = get_task_logger(__name__)
my_logger.setLevel(logging.INFO)
my_handler = logging.FileHandler("logs/my_api.log", encoding = 'utf-8')
my_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
my_handler.setFormatter(my_formatter)
my_logger.addHandler(my_handler)

@app.task
def send_message(send_id):
    send = sender.models.Send.objects.get(pk=send_id)
    clients = sender.models.Client.objects.filter(Q(code=send.code) | Q(tag=send.tag)).distinct()
    for client in clients:
        if now() < send.stop_date:
            sender.models.Message.objects.create(send_id=send, client_id=client)
            my_logger.info('В рамках рассылки %d клиенту %d отправлено сообщение "%s"', send.id, client.id, send.text)
