from django.urls import path
from blog import view

urlpatterns = [
    path('', view.PostView.as_view(), name='home'),
#    path('<slug:slug>/', PostDetail.as_view(), name='post_detail')
    path('<slug:slug>/', view.post_detail, name='post_detail'),
]