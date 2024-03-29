# Generated by Django 3.2.18 on 2023-03-02 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('follower_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.IntegerField()),
                ('reader_id', models.IntegerField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='newsPhotos/%Y/%m/%d')),
                ('text', models.TextField(blank=True)),
                ('bookId', models.IntegerField(blank=True)),
                ('saveStatus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StarList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('post_id', models.IntegerField(blank=True)),
                ('book_id', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserLib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('book_id', models.IntegerField()),
                ('comment', models.TextField(blank=True)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('book_id', models.IntegerField()),
                ('comment', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликованность')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='messenger.category')),
            ],
            options={
                'verbose_name': 'Имеющиеся книги',
                'verbose_name_plural': 'Имеющиеся книги',
                'ordering': ['name'],
            },
        ),
    ]
