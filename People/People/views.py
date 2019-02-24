from django.shortcuts import render
from django.http import JsonResponse
from .forms import SearchForm
from .utilities import search_persons, clean_string


def search_by_keyword(request):
    """
    Search html page which will return results
    :params keyword
    :return: HTML page
    """
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            keyword = str(keyword.lower()).strip()
            keyword = clean_string(keyword)

            if len(keyword) < 3:
                context = {
                    'message': "Insufficient length",
                    'form': form
                }
                return render(request, 'search_dashboard.html', context)
            found, results = search_persons(keyword)
            context = {
                'found': found,
                'results': results,
                'form': form,
            }
            return render(request, 'search_dashboard.html', context)

        else:
            context = {
                'message': "Invalid entry",
                'form': form
            }
            return render(request, 'search_dashboard.html', context)
    else:
        form = SearchForm()
        context = {
            'form': form
        }
        return render(request, 'search_dashboard.html', context)


def search_by_api(request):
    """
    Search html page which will return results
    :params keyword
    :return: json response
    """
    keyword = request.GET.get('keyword')
    keyword = str(keyword.lower()).strip()
    keyword = clean_string(keyword)

    if len(keyword) < 3:
        context = {'error': 'Insufficient length'}
        return JsonResponse(status=400, data=context)
    found, results = search_persons(keyword)
    context = {'found': found, 'results': results }
    return JsonResponse(data=context)
