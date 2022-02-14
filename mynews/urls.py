from django.urls import path
from .import views

#url patterns
urlpatterns = [
    path('', views.index, name="index"),
    path('today', views.news_of_day, name='news_of_day'),
    path('news/archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name = 'pastNews')
]
