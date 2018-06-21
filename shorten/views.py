from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404
from .models import KirrURL
from django.views import View

from .forms import SubmitURLForm
from analytics.models import ClickEvent
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
        context = {
            "title": "Kirr.co",
            "form": form
        }
        template = 'shorten/home.html'
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                'obj': obj,
                'created': created
            }
            if created:
                template = 'shorten/success.html'
            else:
                template = 'shorten/already-exists.html'
        return render(request, template, context)

class KirrRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        #obj = get_object_or_404(KirrURL, shortcode=shortcode)
        qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() !=1 or not qs.exists():
            raise Http404
        print(qs)
        obj = qs.first()
        print(ClickEvent.objects.createcount(obj))
        return HttpResponseRedirect(obj.url)
