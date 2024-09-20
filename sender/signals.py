# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import Client

# @receiver(pre_save, sender=Client)
# def set_code(sender, instance, *args, **kwargs):
#     print(instance.code)
#     instance.code = instance.phone_number[1:4]
#     print(instance.code)

# # @receiver(post_save, sender=Client)
# # def ddd_code(*args, **kwargs):
# #     print("Good!")
