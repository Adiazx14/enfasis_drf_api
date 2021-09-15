from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Article, ArticleSection, Author, Category, Image, Paragraph, Quote

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"

class ParagraphsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = "__all__"

class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ArticleSectionSerializer(serializers.ModelSerializer):
    paragraphs = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    quotes = serializers.SerializerMethodField(read_only=True)
    

    class Meta:
        model = ArticleSection
        fields = "__all__"

    def get_paragraphs(self, obj):
        paragraphs = obj.paragraph_set.all()
        serializer = ParagraphsSerializer(paragraphs, many=True)
        return serializer.data

    def get_images(self, obj):
        images = obj.image_set.all()
        serializer = ImagesSerializer(images, many=True)
        return serializer.data

    def get_quotes(self, obj):
        quotes = obj.quote_set.all()
        serializer = QuotesSerializer(quotes, many=True)
        return serializer.data
 
    

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    sections = serializers.SerializerMethodField(read_only=True)
    category = serializers.SerializerMethodField(read_only=True)
    
    def get_category(self, obj):
        category = obj.category
        serializer = CategorySerializer(category)
        return serializer.data

    class Meta:
        model = Article
        fields = "__all__"

    def get_author(self, obj):
        return str(obj.author)

    def get_sections(self, obj):
        sections = obj.articlesection_set.all()
        serializer = ArticleSectionSerializer(sections, many=True)
        return serializer.data
