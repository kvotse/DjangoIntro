from django.db import models


class Animal(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self) -> str:
        return self.name


class Plant(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

    def __str__(self) -> str:
        return self.name


class Insects(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Насекомое'
        verbose_name_plural = 'Насекомые'

    def __str__(self) -> str:
        return self.name