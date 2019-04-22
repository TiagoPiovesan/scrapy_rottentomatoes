import scrapy
from scrapy_djangoitem import DjangoItem
from movie.models import Movie


class MovieItem(DjangoItem):
    django_model = Movie
    image_urls = scrapy.Field()
    images = scrapy.Field()
