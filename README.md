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

Коллекция Postman для тестирования:

https://konstantteam.postman.co/workspace/KonstantTeam~7addeb6b-acee-447d-84ee-68d6ac50c77e/collection/38299994-988a61d6-bcb5-4c39-80a3-736557a49d2f?action=share&creator=38299994
