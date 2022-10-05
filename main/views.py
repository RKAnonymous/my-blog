from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})


def portfolio(request):
    return render(request, 'portfolio.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def elements(request):
    return render(request, 'elements.html', {})


def portfolio_details(request):
    return render(request, 'portfolio-details.html', {})


def blog_detail(request):
    return render(request, 'single-blog.html', {})


