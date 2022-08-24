from django.shortcuts import render


# Create your views here.
def index(request):
    """ A view to return the index page """
    home_msg = "Hello World"
    print("entered views")
    return render(request, 'customer/index.html', {'msg': home_msg})
