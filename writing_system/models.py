from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    """Абстрактная модель, содержащая поля времени создания и изменения."""
    class Meta:
        abstract = True

    time_create: datetime = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    time_update: datetime = models.DateTimeField(verbose_name='Время изменения', auto_now=True)


class HiraganaLetter(BaseModel):
    class Meta:
        verbose_name = 'Буква хираганы'
        verbose_name_plural = 'Буквы хираганы'

    id: int
    hepburn_romanization = models.CharField('Запись в системе Хепбёрна', max_length=256)
    image = models.ImageField('Изображение буквы', upload_to='hiragana_letters')

    objects: models.Manager


class KatakanaLetter(BaseModel):
    class Meta:
        verbose_name = 'Буква катаканы'
        verbose_name_plural = 'Буквы катаканы'

    id: int
    hepburn_romanization = models.CharField('Запись в системе Хепбёрна', max_length=256)
    image = models.ImageField('Изображение буквы', upload_to='katakana_letters')

    objects: models.Manager


class KanjiLetter(BaseModel):
    class Meta:
        verbose_name = 'Буква кандзи'
        verbose_name_plural = 'Буквы кандзи'

    id: int
    meaning = models.CharField('Значение', max_length=256)
    kunyomi_reading = models.CharField('Кунное чтение', max_length=256, blank=True)
    onyomi_reading = models.CharField('Онное чтение', max_length=256, blank=True)
    image = models.ImageField('Изображение буквы', upload_to='kanji_letters')

    objects: models.Manager
