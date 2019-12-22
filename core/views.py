from django.shortcuts import render


# Create your views here.
from core.models import test


def index(request):
    tests = test.objects.all()
    print(tests)
    return render(request, 'index.html', {'tests':tests})
