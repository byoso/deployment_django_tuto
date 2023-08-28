from django.shortcuts import render

from .models import Sample


def home(request):
    samples = Sample.objects.all()
    context = {
        'samples': samples,
    }
    return render(request, 'app_test/home.html', context)
