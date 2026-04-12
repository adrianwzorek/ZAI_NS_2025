from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from .models import Task, Project
from .forms import TaskForm

# Create your views here.


class TaskListView(ListView):

    model = Task
    template_name = "first_app/task_list.html"
    context_object_name = "tasks"


class TaskDetailView(DetailView):

    model = Task
    template_name = "first_app/task_detail.html"
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    template_name = "first_app/task_form.html"
    form_class = TaskForm

    def get_success_url(self):
        return self.object.get_absolute_url()


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "first_app/task_form.html"
    form_class = TaskForm

    def get_success_url(self):
        return self.object.get_absolute_url()


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "first_app/task_confirm_delete.html"
    success_url = "/"


class ProjectListView(ListView):
    model = Project
    template_name = "first_app/project_list.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "first_app/project_detail.html"
    context_object_name = "project"


class ProjectCreateView(CreateView):
    model = Project
    template_name = "first_app/project_form.html"
    fields = ["name", "description", "is_active"]

    def get_success_url(self):
        return self.object.get_absolute_url()


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "first_app/project_form.html"
    fields = ["name", "description", "is_active"]

    def get_success_url(self):
        return self.object.get_absolute_url()


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "first_app/project_confirm_delete.html"
    success_url = "/projects/"
