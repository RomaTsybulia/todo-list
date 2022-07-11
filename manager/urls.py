from django.urls import path

from manager.views import TaskListView, TagListView, TaskCreateView, \
    TagCreateView, TagUpdateViev, TagDeleteViev, TaskUpdateView, TaskDelteView, \
    update_task_status

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("create-task/", TaskCreateView.as_view(), name="create-task"),
    path("create-tag/", TagCreateView.as_view(), name="create-tag"),
    path("update-tag/<int:pk>/", TagUpdateViev.as_view(), name="update-tag"),
    path("delete-tag/<int:pk>/", TagDeleteViev.as_view(), name="delete-tag"),
    path("update-task/<int:pk>/", TaskUpdateView.as_view(),
         name="update-task"),
    path("delete-task/<int:pk>/", TaskDelteView.as_view(), name="delete-task"),
    path("update-status/<int:pk>", update_task_status,
         name="update_task_status")
]
