from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_scheduled_visits, name='my-scheduled-visits'),
    path('cancellation/<int:id>', views.cancellation, name="cancellation"),
]
