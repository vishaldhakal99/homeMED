from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index2,name = "index2"),
    path('index/', views.index,name = "index"),
    path('doctors/', views.doctors,name = "doctors"),
    path('doctors/<id>/', views.doctorsingle,name = "doctorsingle"),
    path('doctortime/', views.doctortime,name = "doctortime"),
]