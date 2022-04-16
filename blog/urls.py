from ctypes.wintypes import DWORD
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:id>/',views.post_details,name='detail')
]
