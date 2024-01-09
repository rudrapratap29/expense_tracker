from django.urls import path
from .views import *

urlpatterns = [
   path('',index,name='index'),
    path('expense/',show_expenses,name='expense'),
    path('edit/<int:id>/',edit,name='edit'),
    path('delete/<int:id>/',delete,name='delete'),
]