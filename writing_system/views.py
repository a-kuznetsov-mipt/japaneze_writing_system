from django.db.models import QuerySet
from django.views.generic import TemplateView, ListView

from writing_system import models


# Create your views here.

class HomeView(TemplateView):
    """Класс представления начальной страницы сайта."""
    template_name = 'writing_system/home.html'


class HiraganaListView(ListView):
    """Класс представления списка букв хираганы."""
    template_name = 'writing_system/list_hiragana.html'
    context_object_name = 'hiragana_letters'

    def get_queryset(self) -> QuerySet[models.HiraganaLetter]:
        return models.HiraganaLetter.objects.all()


class KatakanaListView(ListView):
    """Класс представления списка букв катаканы."""
    template_name = 'writing_system/list_katakana.html'
    context_object_name = 'katakana_letters'

    def get_queryset(self) -> QuerySet[models.KatakanaLetter]:
        return models.KatakanaLetter.objects.all()


class KanjiListView(ListView):
    """Класс представления списка букв кандзи."""
    template_name = 'writing_system/list_kanji.html'
    context_object_name = 'kanji_letters'
    paginate_by = 50

    def get_queryset(self) -> QuerySet[models.KanjiLetter]:
        return models.KanjiLetter.objects.all()


class HiraganaFormView(TemplateView):
    """Класс представления страницы создания буквы хираганы."""
    template_name = 'writing_system/base.html'


class KatakanaFormView(TemplateView):
    """Класс представления страницы создания буквы катаканы."""
    template_name = 'writing_system/base.html'


class KanjiFormView(TemplateView):
    """Класс представления страницы создания буквы кандзи."""
    template_name = 'writing_system/base.html'


class CreationFromsList(TemplateView):
    """Класс представления страницы списка форм создания букв."""
    template_name = 'writing_system/creation_forms_list.html'
