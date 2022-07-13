from django.urls import path
from . import views
from .views import StaffView


app_name = "staff_list"


urlpatterns = [
    path('', views.index),
    path('staff/', StaffView.as_view()),
    path('staff/<int:pk>', StaffView.as_view()),
]