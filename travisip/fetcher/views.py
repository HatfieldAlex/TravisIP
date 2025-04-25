from django.shortcuts import render, redirect
from .forms import DateRangeForm
from .models import Patent

def patent_search(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            # Save dates to session for a redirect
            request.session['start_date'] = str(start_date)
            request.session['end_date'] = str(end_date)
            return redirect('patent_search')  # Use your URL name here
    else:
        form = DateRangeForm()

    # On GET, check if we just redirected here
    patents = None
    start = request.session.pop('start_date', None)
    end = request.session.pop('end_date', None)
    if start and end:
        patents = Patent.objects.filter(patent_date__range=(start, end))

    return render(request, 'fetcher/patent_search.html', {
        'form': form,
        'patents': patents
    })
