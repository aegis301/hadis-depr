from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

class JavascriptView(TemplateView):
    template_name = "base/javascript.html"
    
    def get_context_data(self, **kwargs):
        return {
            ## TODO: #9 Go on from here with https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-django-react/#the-demo-of-what-well-be-building
        }