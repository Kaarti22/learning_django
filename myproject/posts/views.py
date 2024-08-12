from django.shortcuts import render # type: ignore

# Create your views here.
def posts_list(request):
    return render(request, 'posts/posts_list.html')