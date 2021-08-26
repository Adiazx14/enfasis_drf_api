from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    subtitle = models.CharField(max_length=200, blank=True)

class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    order = models.IntegerField()

class Image(models.Model):
    section = models.ForeignKey(ArticleSection, on_delete=models.CASCADE)
    image = models.ImageField()

class Paragraph(models.Model):
    section = models.ForeignKey(ArticleSection, on_delete=models.CASCADE)
    paragraph = models.TextField()

class Quote(models.Model):
    section = models.ForeignKey(ArticleSection, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, blank=True)
    quote = models.TextField()