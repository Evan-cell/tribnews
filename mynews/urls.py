from django.urls import path
from .import views

#url patterns
urlpatterns = [
    path('', views.news_today, name="news_today"),
    path('news/archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name = 'pastNews')
]
