from django.shortcuts import render
from apps.base.models import Settings
# Create your views here.

def index(request):
    settings = Settings.objects.latest('id')
    return render(request, "index.html", locals())

# 1)Как передавать данные ?
# 2)Куда передавать данные(на какую страницу) ?
# 3) В каком формате будете передавать ?
