from django.shortcuts import render
from .forms import DateRangeForm
from .models import Patent

def patent_search(request):
    patents = None
    form = DateRangeForm()

    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            patents = Patent.objects.filter(patent_date__range=(start_date, end_date))
    # else:
    #     form = DateRangeForm()

    return render(request, 'fetcher/patent_search.html', {'form': form, 'patents': patents})
