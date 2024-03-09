from django.http import HttpResponse
from django.template import loader
from .models import Thesis

def authors(request):
  research_authors = Thesis.objects.all().values()
  template = loader.get_template('all_authors.html')
  context = {
    'research_authors': research_authors,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  research_author = Thesis.objects.get(id=id)
  template = loader.get_template('title_details.html')
  context = {
    'research_author': research_author,
  }
  return HttpResponse(template.render(context, request))