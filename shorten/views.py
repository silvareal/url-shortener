from django.shortcuts import render, get_object_or_404,HttpResponse, HttpResponseRedirect
from .models import KirrURL
from django.views import View

from .forms import SubmitURLForm
# Create your views here.


def home_view(request):
    return render(request, 'shorten/home.html', {})


class ShortenCBV(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        the_form = SubmitURLForm()
        context = {
            'title': 'url shortener',
            'form' : the_form
        }
        return render(request, 'shorten/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        context = {
            'title': 'url shortener',
            'form': form
        }
        return render(request, 'shorten/home.html', context)

