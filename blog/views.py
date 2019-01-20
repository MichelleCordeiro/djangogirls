from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .serializers import PostModelSerializer

from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import PostModelSerializer, AuthTokenSerializer
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

class PostModelViewSet(viewsets.ModelViewSet):
	serializer_class = PostModelSerializer
	queryset = Post.objects.all().order_by('-title')

class CreateTokenView(ObtainAuthToken):
	serializer_class = AuthTokenSerializer
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES