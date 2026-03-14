from django.views.generic import DetailView, ListView
from .models import Task
# Create your views here.



class TaskListView(ListView):

    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"



class TaskDetailView(DetailView):

    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"