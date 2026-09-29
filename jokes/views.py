from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Joke
from .forms import JokeForm
from django.urls import reverse_lazy

# Create your views here.
class JokeListView(ListView):
    model = Joke
    fields = ['question', 'answer']

class JokeDetailView(DetailView):
    model = Joke
    fields = ['question', 'answer']

class JokeCreateView(CreateView):
    model = Joke
    form_class = JokeForm

class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')