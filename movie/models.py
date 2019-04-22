from django.db import models


class Movie(models.Model):
    title = models.CharField('Título',max_length=255, unique=True)
    critics_consensus = models.TextField('Consenso da crítica', blank=True, null=True)
    average_grade = models.DecimalField('Nota média', max_digits=3, decimal_places=2, blank=True, null=True)
    poster = models.ImageField('Capa', blank=True, null=True)
    amount_reviews = models.PositiveIntegerField('Quantidade de criticas', blank=True, null=True)
    approval_percentage = models.PositiveIntegerField('Porcentagem de aprovação', blank=True, null=True)

    def __str__(self):
        return self.title
