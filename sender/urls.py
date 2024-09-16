from django.urls import path
from .views import UserRegistration, UserDetail, UserList, UserDelete, UserDeleteAll


urlpatterns = [
    path('add_client/', ClientAdd.as_view(), name='client-add'),
    path('delete/<int:client_id>/', ClientDelete.as_view(), name='client-delete'),    
    path('client/<int:client_id>/', ClientDetail.as_view(), name='client-detail'),
    path('clients/', ClientList.as_view(), name='client-list'),
    path('add_send/', SendAdd.as_view(), name='send-add'),
    path('delete_send/', SendDelete.as_view(), name='send-delete'),

]
