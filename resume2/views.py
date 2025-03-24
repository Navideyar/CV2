from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about-me.html")

def contact(request):
    return render(request, "contact.html")


def policy(request):
    return render(request, 'policy-and-privacy.html')

def contact(request):
    return render(request, 'contact-me.html')



