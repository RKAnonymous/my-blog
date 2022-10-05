from django.urls import path, include
import main.views as functions

urlpatterns = [
     path('', functions.index, name="index"),
     path('about/', functions.about, name="about"),
     path('elements/', functions.elements, name="elements"),
     path('blog/', functions.blog, name="blog"),
     path('blog-detail/', functions.blog_detail, name="blog_detail"),
     path('services/', functions.services, name="services"),
     path('portfolio/', functions.portfolio, name="portfolio"),
     path('portfolio_details/', functions.portfolio_details, name="portfolio_details"),
]