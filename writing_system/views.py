from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from writing_system import models


# Create your views here.

class HomeView(TemplateView):
    """Класс представления начальной страницы сайта."""
    template_name = 'writing_system/home.html'


class HiraganaListView(ListView):
    """Класс представления списка букв хираганы."""
    template_name = 'writing_system/list_hiragana.html'
    context_object_name = 'hiragana_letters'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[models.HiraganaLetter]:
        return models.HiraganaLetter.objects.all()


class KatakanaListView(ListView):
    """Класс представления списка букв катаканы."""
    template_name = 'writing_system/list_katakana.html'
    context_object_name = 'katakana_letters'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[models.KatakanaLetter]:
        return models.KatakanaLetter.objects.all()


class KanjiListView(ListView):
    """Класс представления списка букв кандзи."""
    template_name = 'writing_system/list_kanji.html'
    context_object_name = 'kanji_letters'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[models.KanjiLetter]:
        return models.KanjiLetter.objects.all()


class HiraganaFormView(CreateView):
    """Класс представления страницы создания буквы хираганы."""
    template_name = 'writing_system/create_hiragana.html'
    model = models.HiraganaLetter
    fields = ['hepburn_romanization', 'image']
    success_url = reverse_lazy('list-hiragana')


class KatakanaFormView(CreateView):
    """Класс представления страницы создания буквы катаканы."""
    template_name = 'writing_system/create_katakana.html'
    model = models.KatakanaLetter
    fields = ['hepburn_romanization', 'image']
    success_url = reverse_lazy('list-katakana')


class KanjiFormView(CreateView):
    """Класс представления страницы создания буквы кандзи."""
    template_name = 'writing_system/create_kanji.html'
    model = models.KanjiLetter
    fields = ['meaning', 'kunyomi_reading', 'onyomi_reading', 'image']
    success_url = reverse_lazy('list-kanji')


class CreationFromsList(TemplateView):
    """Класс представления страницы списка форм создания букв."""
    template_name = 'writing_system/creation_forms_list.html'
