from django.urls import path
from . import views
from .views import NegocioDetailView

urlpatterns = [
    path('', views.base, name="base"),
    path('categoria/<int:category_id>', views.list, name="list"),
    path('<slug:slug>', NegocioDetailView.as_view(), name='detail'),
]
