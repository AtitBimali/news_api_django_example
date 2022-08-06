**Populating Django Website Using an External API**
Check my [Medium Post](https://medium.com/@atitbimali10/populating-django-website-using-an-external-api-46cfdfcb88ec) for more details.

Go to [News API](https://newsapi.org/) and get your API key by signing up or logging in with your Account.

In views.py add your API KEY:
```
API_KEY = 'Your API KEY'
```
We can even save the data from the API to our Database and use it the way we need. 
This way we can create more dynamic page by creating a detail page for the item. 
If you visit the [Books](https://freebiehub.pythonanywhere.com/books/) section of this website and click any of the Book (uses Google Books API) listed there you will be able to see the detail page of that Book.
Leave a Comment below if you want a guide on making a similar page I discussed above.
