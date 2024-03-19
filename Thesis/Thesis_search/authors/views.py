from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Thesis

def landing_page(request):
    return render(request, 'landing_page.html')

def search_results(request):
    query = request.GET.get('query')
    if query:
        # Perform search query processing to retrieve relevant data
        results = Thesis.objects.filter(firstname__icontains=query) | Thesis.objects.filter(lastname__icontains=query)
    else:
        results = None

    return render(request, 'search_results.html', {'query': query, 'results': results})

def members(request):
  mymembers = Thesis.objects.all().values()
  template = loader.get_template('all_authors.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Thesis.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
    authors = []
    all_theses = Thesis.objects.all()
    
    # Collect authors and their theses
    for thesis in all_theses:
        author_name = f"{thesis.firstname} {thesis.lastname}"
        if author_name not in [author['name'] for author in authors]:
            authors.append({
                'name': author_name,
                'firstname': thesis.firstname,
                'lastname': thesis.lastname,
                'theses': [{'title': thesis.title, 'abstract': thesis.abstract}]
            })
        else:
            author = next((author for author in authors if author['name'] == author_name), None)
            if author:
                author['theses'].append({'title': thesis.title, 'abstract': thesis.abstract})

    return render(request, 'main.html', {'authors': authors})


def remaining_authors(request):
    all_authors = Thesis.objects.all()[3:]  # Exclude the first 3 authors
    paginator = Paginator(all_authors, 5)  # Show 5 authors per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'remaining_authors.html', {'page_obj': page_obj})