from django.shortcuts import render



def home(request):
     return render (request,"base/index.html")

def about(request):
     return render (request,"base/about.html")


def blog(request):
     return render (request,"base/blog.html")


def blogdetalle(request):
     return render (request,"base/blogdetalle.html")



def login(request):
     return render (request,"base/login.html")


def registrarse(request):
     return render (request,"base/registrarse.html")    