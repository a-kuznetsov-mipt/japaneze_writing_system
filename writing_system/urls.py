from django.urls import path

from writing_system import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('list_hiragana', views.HiraganaListView.as_view(), name='list-hiragana'),
    path('list_katakana', views.KatakanaListView.as_view(), name='list-katakana'),
    path('list_kanji', views.KanjiListView.as_view(), name='list-kanji'),
    path('create_hiragana', views.HiraganaFormView.as_view(), name='create-hiragana'),
    path('create_katakana', views.KatakanaFormView.as_view(), name='create-katakana'),
    path('create_kanji', views.KanjiFormView.as_view(), name='create-kanji'),
    path('creation_froms_list', views.CreationFromsList.as_view(), name='creation-forms-list'),
]
