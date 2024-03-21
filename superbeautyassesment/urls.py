from django.contrib import admin
from django.urls import path, include
from inventario.views import EquipmentListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/equipment/', EquipmentListView.as_view(), name='equipment-list'),
]
