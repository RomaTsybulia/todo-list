from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from manager.forms import TaskForm
from manager.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("index")


class TaskDelteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")


class TagUpdateViev(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")


class TagDeleteViev(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")


def update_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    if task.done:
        task.done = not task.done
    else:
        task.done = not task.done
    task.save()
    return HttpResponseRedirect(reverse("index"))
