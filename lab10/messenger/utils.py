from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [
    {'title': "Книги", 'url_name': '/main/books'},
    {'title': "Новости", 'url_name': '/'},
    {'title': "Поисковик", 'url_name': '/main/searchPage'},
    {'title': "Добавить книгу", 'url_name': '/main/addBookPage'},
    {'title': "О нас", 'url_name': '/main/about'},
    # {'title': "Главная", 'url_name': '/main'},
]

class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        genres = cache.get('genres')
        cache_menu = cache.get('menu')

        if not self.request.user.is_authenticated:
            user_menu.pop(3)
            cache.set('menu', user_menu, 60)

        if self.request.user.is_authenticated:
            user_menu = menu.copy()
            cache.set('menu', user_menu, 60)

        if not cache_menu:
            cache.set('menu', user_menu, 60)

        if not genres:
            genres = Genre.objects.annotate(Count('books'))
            cache.set('genres', genres, 60)
        # authors = Author.objects.annotate(Count('books'))


        context['menu'] = cache_menu
        context['genres'] = genres
        # context['authors'] = authors
        # context['post'] = post
        if 'genre_selected' not in context:
            context['genre_selected'] = 0
        # if 'author_selected' not in context:
            # context['author_selected'] = 0
        return context