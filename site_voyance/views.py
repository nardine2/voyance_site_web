
from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")

def side_page_right(request):
    return render(request, "sidebar-right.html")

def side_page_left(request):
    return render(request, "sidebar-left.html")

def single(request):
    return render(request, "single.html")
