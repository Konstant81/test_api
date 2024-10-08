from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, ClockedSchedule
from .models import Send
from .tasks import send_message

@receiver(post_save, sender=Send)
def set_task(sender, instance, *args, **kwargs):
    time_now = now()
    if instance.start_date < time_now and instance.stop_date > time_now:
        send_message.delay(instance.id)
    elif instance.start_date >= time_now:
        PeriodicTask.objects.create(name=f"send-{instance.id}",
                                    task="sender.tasks.send_message",
                                    clocked=ClockedSchedule.objects.create(clocked_time=instance.start_date),
                                    args=[instance.id],
                                    one_off=True,)
