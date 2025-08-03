from django.urls import path
from blog import view

urlpatterns = [
    path('', view.PostView.as_view(), name='home')
]