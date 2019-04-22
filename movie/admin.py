from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'average_grade', 'amount_reviews', 'approval_percentage', 'possui_poster', 'possui_critics_consensus')

    def possui_poster(self, obj):
        if obj.poster:
            return 'Sim'
        return 'Não'

        poster.boolean = True

    def possui_critics_consensus(self, obj):
        if obj.critics_consensus:
            return 'Sim'
        return 'Não'

        capa.boolean = True

admin.site.register(Movie, MovieAdmin)