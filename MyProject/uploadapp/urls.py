from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', FileUploadView.as_view()),
    path('load/', FileloadView.as_view()),
    path('update/<int:number>/',FileUpdateView.as_view())

]