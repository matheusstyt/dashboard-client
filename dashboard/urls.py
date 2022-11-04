from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('implantacao/', views.implantacao, name="implantacao"),
    path('comercial/', views.comercial, name="comercial"),
    path('comercial/editarFaturamento/<int:id>', views.editarFaturamento, name="edit-faturamento"),
    path('comercial/deleteFaturamento/<int:id>', views.deleteFaturamento, name="delete-faturamento"),

]
