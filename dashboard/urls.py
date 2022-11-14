from django.urls import path, include

from . import views
from . import plotly_app
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('pipeline/', views.pipeline, name="pipeline"),
    path('pipeline/deletePipelineA/<int:id>', views.pipeline_a_delete, name="delete-pipeline_a_delete"),
    path('pipeline/deletePipelineB/<int:id>', views.pipeline_b_delete, name="delete-pipeline_b_delete"),
    path('pipeline/deletePipelineC/<int:id>', views.pipeline_c_delete, name="delete-pipeline_c_delete"),
    path('pipeline/editPipelineA/<int:id>', views.pipeline_a_edit, name="edit-pipeline_a_edit"),
    path('pipeline/editPipelineB/<int:id>', views.pipeline_b_edit, name="edit-pipeline_b_edit"),
    path('pipeline/editPipelineC/<int:id>', views.pipeline_c_edit, name="edit-pipeline_c_edit"),


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
