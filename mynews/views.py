from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article
from .forms import NewsLetterForm

# Create your views here.
def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
        else:
            form = NewsLetterForm()
                
    return render(request, 'today-news.html',{'date': date,"news":news,"letterForm":form})
print(news_today)



def past_days_news(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)
    
    news = Article.days_news(date)
    return render(request, 'past-news.html', {"date":date,"news":news})
def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html',{"message":message,"articles": searched_articles})
    else:
        message = "you haven't searched for any term"
        return render(request, 'search.html',{"message":message})