from django.urls import path
from . import views
urlpatterns = [
    path('', views.PipelineView),
    path('editPipeline/<int:id>', views.pipeline_edit, name="edit-pipeline_edit"),
    path('deletePipeline/<int:id>', views.pipeline_delete, name="delete-pipeline_edit")
]
