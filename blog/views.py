from django.shortcuts import render

# Create your views hereselfselfself.
def post_list(request):
    return render(request, 'blog/post_list.html')
