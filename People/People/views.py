from django.shortcuts import render
from .database import last_name_index, first_name_index, middle_name_index, persons
from .forms import SearchForm
from .search import Search, explore, suggest
from .serializers import PersonSerializer

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

            # Since there are three columns we need to traverse three trees
            search_objects = [
                Search(first_name_index, keyword),
                Search(middle_name_index, keyword),
                Search(last_name_index, keyword)
                ]

            # Generate results by Levenshtein Automaton based traversal
            found = False
            for search_object in search_objects:
                explore(search_object, search_object.index_tree.root,
                        search_object.max_distance, search_object.search_key)
                found = found or search_object.found

            results = []
            for distance in range(search_objects[0].max_distance+1):
                results.append([])
                count = 0
                for search_object in search_objects:
                    count+=1
                    for result in search_object.results[distance]:
                        results[distance].append(PersonSerializer(persons[result]).data())
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
    pass
