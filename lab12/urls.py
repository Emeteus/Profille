
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from main import views as viewsIndex

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewsIndex.index, name='home'),
    path('<str:codde>/', viewsIndex.singer_detail, name='singer_detail'),
]
