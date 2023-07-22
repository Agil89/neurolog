# from django.views.generic import TemplateView
from django.shortcuts import render, redirect
# from .models import Package, Slider, Advantages, Blogs, AboutUs


def index(request):
    context = {}
    # context['slider'] = Slider.objects.last()
    # context['packages'] = Package.objects.all()
    # context['advantages'] = Advantages.objects.all()
    return render(request, 'index.html', context)