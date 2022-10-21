from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import News
from .serializers import NewsSerializers


def home(request):
    return render(request=request, template_name='index.html', context={})


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
