from django.views.generic import TemplateView


# Create your views here.

class HomeView(TemplateView):
    """Класс представления начальной страницы сайта."""
    template_name = 'writing_system/base.html'


class HiraganaListView(TemplateView):
    """Класс представления списка букв хираганы."""
    template_name = 'writing_system/base.html'


class KatakanaListView(TemplateView):
    """Класс представления списка букв катаканы."""
    template_name = 'writing_system/base.html'


class KanjiListView(TemplateView):
    """Класс представления списка букв кандзи."""
    template_name = 'writing_system/base.html'


class HiraganaFormView(TemplateView):
    """Класс представления страницы создания буквы хираганы."""
    template_name = 'writing_system/base.html'


class KatakanaFormView(TemplateView):
    """Класс представления страницы создания буквы хираганы."""
    template_name = 'writing_system/base.html'


class KanjiFormView(TemplateView):
    """Класс представления страницы создания буквы хираганы."""
    template_name = 'writing_system/base.html'
