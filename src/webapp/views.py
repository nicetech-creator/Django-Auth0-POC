from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'webapp/index.html', context)

@login_required
def profile(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }

    return render(request, 'webapp/profile.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })