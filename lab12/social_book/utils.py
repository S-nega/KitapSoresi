from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [
    {'title': "Книги", 'url_name': '/main/books'},
    {'title': "Добавить книгу", 'url_name': '/main/uploadbook'},
    {'title': "Новости", 'url_name': '/'},
    {'title': "Поисковик", 'url_name': '/search'},
    # {'title': "О нас", 'url_name': '/main/about'},
    # {'title': "Главная", 'url_name': '/main'},
]

class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        # posts = cache.get('posts')
        cache_menu = cache.get('menu')

        if not self.request.user.is_authenticated:
            del user_menu[1:4]
            cache.set('menu', user_menu, 60)

        if self.request.user.is_authenticated:
            user_menu = menu.copy()
            cache.set('menu', user_menu, 60)

        if not cache_menu:
            cache.set('menu', user_menu, 60)

        # if not posts:
        #     posts = Post.objects.annotate
        #     cache.set('posts', posts, 60)
        # # authors = Author.objects.annotate(Count('books'))


        context['menu'] = cache_menu
        context['posts'] = Post.objects.annotate()
        # if 'genre_selected' not in context:
        #     context['genre_selected'] = 0
        return context