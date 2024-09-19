from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
# from django.forms import ValidationError


class Client(models.Model):
    # def code_validation(self):
    #     print(self)
    #     if len(self) > 3 or len(self) < 1 or not self.isdigit():
    #         raise ValidationError('Код оператора должен иметь числовое значение и находиться в диапазоне 001...999')
    
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^7\d{10}$', message='Введите телефон в формате 7ХХХХХХХХХХ')])     # Номер телефона
    code = models.CharField(blank=True)                           # Код мобильного оператора
    tag = models.CharField(max_length=100, default= None, blank=True)                                                                                 # метка

    class Meta:
        db_table = "client" # Имя таблицы в БД
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

class Send(models.Model):
    start_date = models.DateTimeField()                                                                        # Время и дата запуска рассылки
    stop_date = models.DateTimeField()                                                                         # Время и дата окончания рассылки
    text = models.CharField(max_length=100)                                                                    # Текст сообщения
    code = models.CharField(validators=[MinLengthValidator(limit_value=3), MaxLengthValidator(limit_value=3)]) # Код мобильного оператора
    tag = models.CharField(max_length=100, default= None)                                                      # метка

    class Meta:
        db_table = "send" # Имя таблицы в БД
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        
class Message(models.Model):
    send_date = models.DateTimeField(auto_now_add=True)                                        # Время отправки сообщения
    send_id = models.ForeignKey(Send, on_delete=models.DO_NOTHING, verbose_name='рассылка')    # ID рассылки
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING, verbose_name='клиент')  # ID клиента

    class Meta:
        db_table = "message" # Имя таблицы в БД
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
