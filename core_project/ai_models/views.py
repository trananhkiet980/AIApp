from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import AiModel

class AiModelListView(ListView):
    model = AiModel
    template_name = 'ai_models/ai_list.html'
    context_object_name = 'models'

class AiModelCreateView(CreateView):
    model = AiModel
    template_name = 'ai_models/ai_form.html'
    fields = ['name', 'framework', 'description']

class AiModelUpdateView(UpdateView):
    model = AiModel
    template_name = 'ai_models/ai_form.html'
    fields = ['name', 'framework', 'description']

class AiModelDeleteView(DeleteView):
    model = AiModel
    template_name = 'ai_models/ai_confirm_delete.html'
    success_url = reverse_lazy('ai_list')