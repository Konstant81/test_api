Сервис управления рассылками.

После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания из справочника будут выбраны все клиенты,
которые подходят под значения фильтра (код оператора, тег), указанного в этой рассылке и запущена отправка для всех этих клиентов.

Если создаётся рассылка с временем старта в будущем - отправка стартует автоматически по наступлению этого времени без дополнительных действий со стороны пользователя системы.

Сообщения рассылки выводятся в файл logs/my_api.log.

Используемые технологии: 
- Python
- Django
- Django Rest Framework
- Celery
- Celery Beat
- Redis
- Docker
- PostgreSQL

Коллекция Postman для тестирования находится в репозитории.
