from .models import *
from .views import *
from django import views
from django.urls import path

app_name = 'listing'

urlpatterns = [
    path('', index, name='home'),
    path('<int:list_id>', detailed, name='detailed'),
    path('contact', contact_view, name='contact'),

]
