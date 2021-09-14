from api.serializers import ArticleSerializer
from api.models import Article
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView, status

class ArticleList(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleDetail(APIView):

    def get(self, request, id):
        article = Article.objects.get(id=id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)