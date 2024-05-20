# Generated by Django 4.1.7 on 2024-05-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HiraganaLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('hepburn_romanization', models.CharField(max_length=256, verbose_name='Запись в системе Хепбёрна')),
                ('image', models.ImageField(upload_to='hiragana_letters', verbose_name='Изображение буквы')),
            ],
            options={
                'verbose_name': 'Буква хираганы',
                'verbose_name_plural': 'Буквы хираганы',
            },
        ),
        migrations.CreateModel(
            name='KanjiLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('meaning', models.CharField(max_length=256, verbose_name='Значение')),
                ('kunyomi_reading', models.CharField(blank=True, max_length=256, verbose_name='Кунное чтение')),
                ('onyomi_reading', models.CharField(blank=True, max_length=256, verbose_name='Онное чтение')),
                ('image', models.ImageField(upload_to='kanji_letters', verbose_name='Изображение буквы')),
            ],
            options={
                'verbose_name': 'Буква кандзи',
                'verbose_name_plural': 'Буквы кандзи',
            },
        ),
        migrations.CreateModel(
            name='KatakanaLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('hepburn_romanization', models.CharField(max_length=256, verbose_name='Запись в системе Хепбёрна')),
                ('image', models.ImageField(upload_to='katakana_letters', verbose_name='Изображение буквы')),
            ],
            options={
                'verbose_name': 'Буква катаканы',
                'verbose_name_plural': 'Буквы катаканы',
            },
        ),
    ]