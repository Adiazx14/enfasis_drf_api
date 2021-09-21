from django.http.response import HttpResponse
from api.serializers import ArticleSerializer, RevistaSerializer
from api.models import Article, Revista
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
        try:
            article = Article.objects.get(id=id)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

class RevistasView(APIView):

    def get(self, request):
        revistas = Revista.objects.all()
        serializer = RevistaSerializer(revistas, many=True)
        return Response(serializer.data) 