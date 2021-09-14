from .views import ArticleDetail, ArticleList
from django.urls import path

urlpatterns = [
    path('', view=ArticleList.as_view()),
    path('<int:id>/', ArticleDetail.as_view())
]