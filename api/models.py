from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    subtitle = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    order = models.IntegerField()

    def __str__(self):
        return  str(self.article) + " (" + str(self.order) + ")"



class Paragraph(models.Model):
    section = models.ForeignKey(ArticleSection, on_delete=models.CASCADE)
    paragraph = models.TextField()

class Quote(models.Model):
    section = models.ForeignKey(ArticleSection, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, blank=True)
    quote = models.TextField()

class Revista(models.Model):
    file = models.FileField(upload_to='files/')
    number = models.IntegerField()
    author = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    paragraph = models.TextField(blank=True)

    def __str__(self):
        return f'Número {self.number} ({self.subtitle})'

class Image(models.Model):
    section = models.ForeignKey(ArticleSection, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE, null=True, blank=True)
    caption = models.CharField(max_length=200, blank=True)
    image = models.ImageField()