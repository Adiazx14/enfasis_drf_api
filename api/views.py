from django.http.response import HttpResponse
from rest_framework import serializers
from api.serializers import ArticleSerializer, PromotionSerializer, RevistaSerializer, SubscriberSerializer
from api.models import Article, Promotion, Revista, Subscriber
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView, status

class ArticleList(APIView):

    def get(self, request):
        articles = Article.objects.all().order_by("-id")
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

class SubscriberView(APIView):

    def get(self, request):
        subscriber = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscriber, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SubscriberSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PromotionView(APIView):

    def get(self, request):
        promotions = Promotion.objects.all()
        serializer = PromotionSerializer(promotions, many = True)
        return Response(serializer.data)