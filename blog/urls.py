from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('list/', views.list, name="list"),
    path('detail/<int:id>/', views.detail, name="detail")
]

"""
localhost:8000/blog/list/
localhost:8000/blog/detail/1
"""