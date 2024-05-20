from django.urls import path

from writing_system import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('list_hiragana', views.HiraganaListView.as_view(), name='list-hiragana'),
    path('list_katakana', views.KatakanaListView.as_view(), name='list-katakana'),
    path('list_kanji', views.KanjiListView.as_view(), name='list-kanji'),
    path('from_hiragana', views.HiraganaListView.as_view(), name='form-hiragana'),
    path('form_katakana', views.KatakanaListView.as_view(), name='form-katakana'),
    path('form_kanji', views.KanjiListView.as_view(), name='form-kanji'),
]
