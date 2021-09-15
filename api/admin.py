from django.contrib import admin
from django.db import models
from .models import Article, ArticleSection, Author, Category, Image, Paragraph, Quote, Revista

class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection

class ArticleAdmin(admin.ModelAdmin):
    model= Article
    inlines=[ArticleSectionInline]

class ParagraphsInline(admin.TabularInline):
    model=Paragraph

class ImagesInline(admin.TabularInline):
    model=Image

class QuotesInline(admin.TabularInline):
    model=Quote

class ArticleSectionAdmin(admin.ModelAdmin):
    model=ArticleSection
    inlines=[ParagraphsInline, ImagesInline, QuotesInline]

class RevistaAdmin(admin.ModelAdmin):
    model = Revista
    inlines = [ImagesInline]


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleSection,ArticleSectionAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Revista, RevistaAdmin)