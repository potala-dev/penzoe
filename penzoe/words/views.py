from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from .models import Word


class WordDetailView(LoginRequiredMixin, DetailView):

    model = Word
    context_object_name = "word"


word_detail_view = WordDetailView.as_view()


class WordListView(LoginRequiredMixin, ListView):

    model = Word
    context_object_name = "words"


word_list_view = WordListView.as_view()
