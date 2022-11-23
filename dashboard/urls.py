from django.urls import path, include

from . import views
from . import plotly_app
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('implantacao/', views.implantacao, name="implantacao"),
    path('implantacao/planejado/<int:id>', views.implantacao_planejado_edit, name="edit-planejado"),
    path('implantacao/curso/<int:id>', views.implantacao_curso_edit, name="edit-curso"),
    path('implantacao/concluido/<int:id>', views.implantacao_concluido_edit, name="edit-concluido"),

    path('implantacao/planejadoDel/<int:id>', views.implantacao_planejado_delete, name="delete-planejado"),
    path('implantacao/cursoDel/<int:id>', views.implantacao_curso_delete, name="delete-curso"),
    path('implantacao/concluidoDel/<int:id>', views.implantacao_concluido_delete, name="delete-concluido"),

    path('comercial/', views.comercial, name="comercial"),
    path('comercial/editarFaturamento/<int:id>', views.editarFaturamento, name="edit-faturamento"),
    path('comercial/deleteFaturamento/<int:id>', views.deleteFaturamento, name="delete-faturamento"),
    path('comercial/editarMeta/<int:id>', views.editarMeta, name="edit-meta"),

]
