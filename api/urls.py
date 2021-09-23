from rest_framework import views
from .views import ArticleDetail, ArticleList, RevistasView, SubscriberView
from django.urls import path

urlpatterns = [
    path('', view=ArticleList.as_view()),
    path('<int:id>/', view=ArticleDetail.as_view()),
    path('revistas/', view=RevistasView.as_view()),
    path('subscribers/', view=SubscriberView.as_view())
]