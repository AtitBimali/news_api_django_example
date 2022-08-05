from django.shortcuts import get_object_or_404, render
from .models import *
import requests
import os
from dotenv import load_dotenv
load_dotenv()
def news(request):
    API_KEY = os.getenv('API_KEY') 

    print("Hello")
    print(f"{API_KEY}")

    country = request.GET.get('country')
    category = request.GET.get('category')
    item = request.GET.get('item')
    
    if country:
        if country == 'india':
            country = 'in'
        elif country == 'usa':
            country = 'us'
        elif country == 'uae':
            country = 'ae'
        elif country == 'argentina':
            country = 'ar'
        elif country == 'nepal':
            country = 'np'
        elif country == 'austria':
            country = 'at'
        elif country == 'japan':
            country = 'jp'
        elif country == 'england':
            country = 'eg'
        elif country == 'china':
            country = 'cn'
        elif country == 'mexico':
            country = 'mx'
        elif country == 'russia':
            country = 'rs'
        elif country == 'korea':
            country = 'kr'

        url = f"https://newsapi.org/v2/top-headlines?country={country}&sortBy=publishedAt&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category:
        url = f"https://newsapi.org/v2/top-headlines?category={category}&sortBy=publishedAt&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif item:
        url = f"https://newsapi.org/v2/everything?q={item}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        

    else:
        url = f"https://newsapi.org/v2/top-headlines?country=us&sortBy=publishedAt&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context ={
        'articles': articles
    }
    return render (request,'news_app/home.html',context)

